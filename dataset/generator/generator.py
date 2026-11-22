"""Turn one MSLIB instance into an automotive-style project with explicit modes.

Each rule has a switch in GeneratorSettings, so its effect can be measured alone:
  base           PERT durations per mode from the work-content rule, departments, dedication rules, mode cap
  constraints    random team constraints: barred workers per task and incompatible worker pairs
  reviewer       review tasks staffed only from an independent quality department (ISO 26262 style independence)
  extra_workers  sparse modes with one extra worker on long tasks, with a coordination overhead and a duration floor
  liaison        one liaison worker with an external-communication skill; its tasks get a long right tail
  rewire         the precedence graph rewired: the same number of edges, more of them long-range

Every time is in units of 1 / time_unit days (quarter days by default), so the PERT shape, not the rounding of
D = ceil(X), drives the risk. The deadline is left as a technical horizon; set it with with_deadline once the
reference makespan is known.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass, field, replace
from graphlib import TopologicalSorter
import math

import numpy as np

from planner.core.distributions import DurationDistribution, register_distribution
from planner.core.project import Deadline, Mode, Project, Task, Worker
from planner.core.validation import validate_project
from dataset.generator.mslib import MSInstance

RULES = ('constraints', 'reviewer', 'extra_workers', 'liaison', 'rewire')


@dataclass(frozen=True)
class GeneratorSettings:
    """Generator parameters; the defaults generate the paper's instances (with uncertainty=2.0)."""

    seed: int = 0
    time_unit: int = 4  # Units per day: quarter days.
    mode_cap: int = 32  # At most this many modes per task.
    uncertainty: float = 1.0  # Multiplies every PERT spread; 2.0 is the high-uncertainty setting.

    # Durations: work content d x team size over the team's effective rate, times a random factor per mode
    mode_factor_sigma: float = 0.15  # Standard deviation of the log of the factor per mode.
    level_effect: float = 0.1  # Efficiency change per skill level above or below the required level.
    efficiency_bounds: tuple[float, float] = (0.7, 1.4)
    # Risk classes of tasks: (probability, spread below the most likely value, spread above it)
    risk_classes: tuple[tuple[float, float, float], ...] = ((0.5, 0.1, 0.3), (0.35, 0.15, 0.6), (0.15, 0.2, 1.2))
    mode_spread_jitter: float = 0.3  # The upper spread varies by up to this share between modes.
    speed_risk_exponent: float = 3.0  # A faster mode (factor below 1) gets a longer right tail: factor ** -exponent.

    # Teams and dedication
    department_size: int = 6  # Workers per department, about an automotive team.
    cross_department_share: float = 0.1  # Share of sampled teams drawn across departments.
    dedication_levels: tuple[float, ...] = (0.5, 0.75, 1.0)  # At least half time for every worker.
    dedication_weights: tuple[float, ...] = (0.2, 0.3, 0.5)
    safety_skill: bool = True  # One random skill is safety-critical and always needs full time.

    # Rule switches
    constraints: bool = True
    reviewer: bool = True
    extra_workers: bool = True
    liaison: bool = True
    rewire: bool = True

    # Rule parameters
    barred_share: float = 0.05  # Share of (task, qualified worker) pairs barred.
    incompatible_pairs_per_worker: float = 0.1  # Incompatible pairs per worker.
    review_task_share: float = 0.15
    quality_share: float = 0.15  # Share of workers in the quality department.
    review_dedication: tuple[float, ...] = (0.25, 0.5)
    extra_share: float = 0.3  # Share of the longer half of tasks that get extra-worker modes.
    extra_overhead: float = 0.1  # Coordination overhead per extra worker.
    extra_floor: float = 0.75  # An extra-worker mode is never faster than this share of the base duration.
    liaison_task_share: float = 0.1
    liaison_dedication: tuple[float, ...] = (0.25, 0.5)
    liaison_upper_spread: float = 2.0  # Liaison tasks reach up to three times the most likely duration.
    rewire_share: float = 0.3  # Share of edges between real tasks that is replaced.
    long_range_share: float = 1 / 3  # New edges span at least this share of the topological order.

    dedication_variants: int = 3  # Dedication patterns drawn per team; the same team at half time is another mode.
    separate_quality_from: int = 12  # Below this many workers, quality workers also join regular tasks.
    attempts_per_mode: int = 30  # Team samples per wanted mode before giving up.

    def only(self, *rules: str) -> 'GeneratorSettings':
        """Return the settings with exactly these rules switched on (none: the base settings)."""
        unknown = set(rules) - set(RULES)
        if unknown:
            raise ValueError(f'unknown rules: {sorted(unknown)}')
        return replace(self, **{rule: rule in rules for rule in RULES})


@dataclass
class GeneratedInstance:
    """A generated project and what the generator decided, for the scenario file and the report."""

    project: Project
    source_id: str
    settings: GeneratorSettings
    details: dict = field(default_factory=dict)

    def configuration(self) -> dict:
        """The scenario file's Configuration block."""
        return dict(generator='dataset.generator.generator', source_id=self.source_id,
                    settings=asdict(self.settings), details=self.details, n_workers=len(self.project.workers),
                    n_tasks=len(self.project.tasks), n_skills=0, seed=self.settings.seed)


def generate(instance: MSInstance, settings: GeneratorSettings = GeneratorSettings()) -> GeneratedInstance:
    """Generate one project from an MSLIB instance; the same instance and settings give the same project."""
    number = int(instance.instance_id.rsplit('_', 1)[1])
    set_number = int(instance.instance_id.split('_')[1].removeprefix('Set'))
    rng = np.random.default_rng([settings.seed, set_number, number])
    modules = {section.name: section.rows for section in instance.sections}
    levels = modules['Workforce Module with Skill Levels']
    required_levels = modules['Skill Level Requirements Module']
    n_workers, n_skills = len(instance.worker_skills), instance.n_skills
    real = instance.activities[1:-1]
    details: dict = defaultdict(int)

    # Workers, their skills and levels; the liaison worker gets an extra skill index
    workers = [f'worker_{w}' for w in range(1, n_workers + 1)]
    skills = {workers[w]: {k for k in range(n_skills) if instance.worker_skills[w][k]} for w in range(n_workers)}
    level = {(workers[w], k): levels[w][k] for w in range(n_workers) for k in range(n_skills)}

    # Departments: workers sorted by their strongest skill, then cut into departments of about department_size
    quality: set[str] = set()
    if settings.reviewer:
        count = max(1, round(settings.quality_share * n_workers))
        quality = set(_pick(rng, workers, min(count, n_workers - 1))) if n_workers > 1 else set()
    regular = sorted((w for w in workers if w not in quality),
                     key=lambda w: (max(range(n_skills), key=lambda k: level[w, k]), int(w.split('_')[1])))
    n_departments = max(1, math.ceil(len(regular) / settings.department_size))
    department = {w: min(i * n_departments // len(regular), n_departments - 1) for i, w in enumerate(regular)}
    department.update({w: n_departments for w in quality})  # The quality department is the last one.

    # Rule choices per task
    safety = int(rng.integers(n_skills)) if settings.safety_skill else None
    task_ids = [f'task_{activity.id}' for activity in real]
    barred = {t: set() for t in task_ids}
    incompatible: set[frozenset] = set()
    if settings.constraints:
        for activity, t in zip(real, task_ids):
            needed = {k for k, c in enumerate(activity.skill_requirements) if c}
            for w in workers:
                if skills[w] & needed and rng.random() < settings.barred_share:
                    barred[t].add(w)
        n_pairs = round(settings.incompatible_pairs_per_worker * n_workers)
        for _ in range(n_pairs):
            if n_workers > 1:
                incompatible.add(frozenset(_pick(rng, workers, 2)))
    review = set()
    if settings.reviewer and quality:
        staffable = [t for activity, t in zip(real, task_ids)
                     if _can_cover(activity, [w for w in workers if w in quality], skills)]
        count = round(settings.review_task_share * len(real))
        review = set(_pick(rng, staffable, min(count, len(staffable))))
    liaison_worker = f'worker_{n_workers + 1}' if settings.liaison else None
    liaison_tasks = set()
    if liaison_worker:
        count = max(1, round(settings.liaison_task_share * len(real)))
        liaison_tasks = set(_pick(rng, task_ids, min(count, len(task_ids))))
    median = float(np.median([activity.duration for activity in real]))
    extra_tasks = {t for activity, t in zip(real, task_ids)
                   if settings.extra_workers and activity.duration > median and rng.random() < settings.extra_share}

    # Modes and their duration distributions
    distributions: dict[str, DurationDistribution] = {}
    milestone_key = register_distribution(distributions, DurationDistribution('tabular', probabilities={0: 1.0}))
    tasks = []
    for activity in instance.activities:
        t = f'task_{activity.id}'
        if activity is instance.activities[0] or activity is instance.activities[-1]:
            tasks.append(Task(t, (Mode(1, {}, milestone_key),), milestone=True))
            continue
        positions = [k for k, count in enumerate(activity.skill_requirements) for _ in range(count)]
        position_levels = list(required_levels[activity.id - 1]) if positions else []
        risk = settings.risk_classes[rng.choice(len(settings.risk_classes),
                                                p=[c[0] for c in settings.risk_classes])]
        teams = _sample_teams(rng, settings, positions, workers, skills, department, quality, barred[t],
                              incompatible, t in review, details)
        # Candidate modes: each team (and its extra-worker variant) with several dedication patterns
        candidates, seen = [], set()
        for team in teams:
            variants = [team]
            if t in extra_tasks:
                extra = _extra_worker(rng, team, positions, workers, skills, department, quality, barred[t],
                                      incompatible, t in review)
                if extra is not None:
                    variants.append(team + [extra])
            for members in variants:
                for _ in range(settings.dedication_variants):
                    dedication = {}
                    for w, k in members:
                        if t in review:
                            dedication[w] = float(rng.choice(settings.review_dedication))
                        elif safety is not None and k == safety:
                            dedication[w] = 1.0
                        else:
                            dedication[w] = float(rng.choice(settings.dedication_levels, p=settings.dedication_weights))
                    if liaison_worker and t in liaison_tasks:
                        dedication[liaison_worker] = float(rng.choice(settings.liaison_dedication))
                    key = frozenset(dedication.items())
                    if key not in seen:
                        seen.add(key)
                        candidates.append((members, dedication))
        # Keep at most mode_cap, first one pattern per team so every sampled team stays available
        first = {}
        for index, (members, _) in enumerate(candidates):
            first.setdefault(frozenset(w for w, _ in members), index)
        ranked = sorted(range(len(candidates)), key=lambda i: (i not in first.values(), rng.random()))
        modes = []
        for index in sorted(ranked[:settings.mode_cap]):
            members, dedication = candidates[index]
            distribution = _mode_distribution(rng, settings, activity.duration, members, positions,
                                              position_levels, level, dedication, risk, t in liaison_tasks)
            modes.append(Mode(len(modes) + 1, dedication, register_distribution(distributions, distribution)))
        details['modes'] += len(modes)
        details['tasks_at_cap'] += len(modes) >= settings.mode_cap
        tasks.append(Task(t, tuple(modes)))

    # Precedence: the source edges, rewired between real tasks when asked
    edges = [(f'task_{a.id}', f'task_{s}') for a in instance.activities for s in a.successors]
    if settings.rewire:
        edges = _rewire(rng, settings, edges, task_ids, f'task_{instance.activities[0].id}',
                        f'task_{instance.activities[-1].id}', details)

    all_workers = tuple(Worker(w) for w in workers) + ((Worker(liaison_worker),) if liaison_worker else ())
    horizon = settings.time_unit * max(1, sum(10 * a.duration * max(1, sum(a.skill_requirements)) for a in real))
    project = Project(all_workers, tuple(tasks), tuple(edges), Deadline(horizon), distributions,
                      n_dedication_levels=4)
    report = validate_project(project)
    if not report.is_correct:
        raise ValueError(f'{instance.instance_id}: generated project is incorrect: ' + '; '.join(report.errors))
    details.update(departments=n_departments, quality=sorted(quality, key=lambda w: int(w.split('_')[1])),
                   safety_skill=safety, review_tasks=len(review), liaison_tasks=len(liaison_tasks),
                   extra_tasks=len(extra_tasks), barred_pairs=sum(map(len, barred.values())),
                   incompatible_pairs=len(incompatible), edges=len(edges))
    return GeneratedInstance(project, instance.instance_id, settings, dict(details))


def with_deadline(project: Project, factor: float, reference: int) -> Project:
    """Return the project with deadline floor(factor x reference makespan)."""
    return replace(project, deadline=Deadline(math.floor(factor * reference + 1e-9)), validation=None)


def _pick(rng, items, count):
    """count distinct items drawn at random, as plain Python values."""
    return [items[i] for i in rng.choice(len(items), size=count, replace=False)]


# Teams

def _can_cover(activity, pool, skills) -> bool:
    """Whether some distinct workers of the pool fill every required skill position (greedy is enough to check)."""
    positions = [k for k, count in enumerate(activity.skill_requirements) for _ in range(count)]
    return _fill(positions, pool, skills, None) is not None


def _fill(positions, pool, skills, rng, excluded=frozenset()):
    """Fill positions with distinct workers by augmenting paths; random order when rng is given."""
    order = list(pool)
    if rng is not None:
        order = [order[i] for i in rng.permutation(len(order))]
    assigned: dict[int, str] = {}
    holder: dict[str, int] = {}

    def augment(position, visited):
        for w in order:
            if w in excluded or positions[position] not in skills[w] or w in visited:
                continue
            visited.add(w)
            if w not in holder or augment(holder[w], visited):
                assigned[position], holder[w] = w, position
                return True
        return False

    for position in range(len(positions)):
        if not augment(position, set()):
            return None
    return [(assigned[p], positions[p]) for p in range(len(positions))]


def _sample_teams(rng, settings, positions, workers, skills, department, quality, barred, incompatible, review, details):
    """Sample up to mode_cap distinct teams as [(worker, skill)], relaxing rules only when none is found.

    Departments first, a few teams across departments; a review task draws from the quality department only.
    Relaxations, in order: across departments, then without random constraints, then any qualified worker.
    """
    if not positions:
        return [[]]
    departments = sorted(set(department.values()))
    quality_department = max(departments) if quality else None
    regular = [d for d in departments if d != quality_department] or departments

    shared_quality = len(workers) < settings.separate_quality_from

    def pools():
        if review:
            return [w for w in workers if w in quality]
        if rng.random() < settings.cross_department_share:
            return [w for w in workers if w not in quality or shared_quality]
        home = regular[rng.integers(len(regular))]
        return [w for w in workers if department[w] == home or (shared_quality and w in quality)]

    def allowed(team):
        names = {w for w, _ in team}
        return not any(pair <= names for pair in incompatible)

    teams, seen = [], set()
    for _ in range(settings.attempts_per_mode * settings.mode_cap):
        team = _fill(positions, pools(), skills, rng, excluded=barred)
        if team is None or not allowed(team):
            continue
        key = frozenset(w for w, _ in team)
        if key not in seen:
            seen.add(key)
            teams.append(team)
            if len(teams) >= settings.mode_cap:
                break
    if teams:
        return teams

    # Relax step by step, recording which relaxation was needed
    others = [w for w in workers if w in quality] if review else [w for w in workers if w not in quality or shared_quality]
    for name, pool, excluded, check in (
            ('relaxed_department', others, barred, allowed),
            ('relaxed_constraints', others, frozenset(), lambda team: True),
            ('relaxed_all', workers, frozenset(), lambda team: True)):
        for _ in range(settings.attempts_per_mode):
            team = _fill(positions, pool, skills, rng, excluded=excluded)
            if team is not None and check(team):
                details[name] += 1
                return [team]
    raise ValueError('no qualified team exists for a task')


def _extra_worker(rng, team, positions, workers, skills, department, quality, barred, incompatible, review):
    """One more worker for a long task: qualified for one of its skills, from the same department as the team."""
    members = {w for w, _ in team}
    home = {department[w] for w, _ in team}
    needed = sorted(set(positions))
    candidates = [(w, k) for w in workers for k in needed
                  if w not in members and w not in barred and k in skills[w] and department[w] in home
                  and (w in quality) == review and not any(pair <= members | {w} for pair in incompatible)]
    # On small instances the quality department is too small for a home department; any regular worker may help
    if not candidates and not review:
        candidates = [(w, k) for w in workers for k in needed if w not in members and w not in barred
                      and k in skills[w] and not any(pair <= members | {w} for pair in incompatible)]
    if not candidates:
        return None
    return candidates[rng.integers(len(candidates))]


# Durations

def _mode_distribution(rng, settings, duration, members, positions, position_levels, level, dedication, risk,
                       is_liaison_task):
    """PERT in time units: most likely value from the work-content rule and a random factor, spreads from the risk."""
    # Work content: the source duration times the team size it was set for; the rate counts dedication and skill level
    work = duration * max(1, len(positions))
    rate = 0.0
    for index, (w, k) in enumerate(members):
        required = position_levels[index] if index < len(position_levels) else level[w, k]
        efficiency = 1 + settings.level_effect * (level[w, k] - required)
        rate += dedication[w] * min(max(efficiency, settings.efficiency_bounds[0]), settings.efficiency_bounds[1])
    most_likely = work / max(rate, 1e-9)
    extras = max(0, len(members) - len(positions))
    if extras:
        most_likely = max(most_likely * (1 + settings.extra_overhead * extras), settings.extra_floor * duration)
    factor = float(np.exp(rng.normal(0, settings.mode_factor_sigma)))
    most_likely *= factor

    # Spreads: the task's risk class, jittered per mode, longer for faster modes and for liaison tasks
    _, low, high = risk
    jitter = 1 + settings.mode_spread_jitter * float(rng.uniform(-1, 1))
    high = high * jitter * factor ** -settings.speed_risk_exponent
    if is_liaison_task:
        high = max(high, settings.liaison_upper_spread)
    low, high = min(0.9, low * settings.uncertainty), high * settings.uncertainty
    unit = settings.time_unit
    return DurationDistribution('pert', dict(a=unit * most_likely * (1 - low), b=unit * most_likely,
                                             c=unit * most_likely * (1 + high)))


# Precedence

def _rewire(rng, settings, edges, task_ids, start, end, details):
    """Swap a share of the edges between real tasks for long-range ones, keeping their number and acyclicity.

    Each swap removes a random edge and adds an edge that goes forward in the original topological order, spans at
    least long_range_share of it, and is not implied by existing paths; a swap with no such edge is undone. The
    dummy start and end are reconnected to tasks without predecessors or successors.
    """
    real = set(task_ids)
    inner = [e for e in edges if e[0] in real and e[1] in real]
    predecessors = {t: set() for t in task_ids}
    for before, after in inner:
        predecessors[after].add(before)
    order = list(TopologicalSorter(predecessors).static_order())
    position = {t: i for i, t in enumerate(order)}
    n = len(order)
    gap = max(1, round(settings.long_range_share * n))

    def closure(edge_list):
        """reach[i] is a bitmask of the tasks reachable from task i (positions in the original order)."""
        successors = defaultdict(list)
        for before, after in edge_list:
            successors[position[before]].append(position[after])
        reach = [0] * n
        for i in reversed(range(n)):
            for j in successors[i]:
                reach[i] |= (1 << j) | reach[j]
        return reach

    current = list(inner)
    swaps = 0
    for _ in range(round(settings.rewire_share * len(inner))):
        removed = current.pop(int(rng.integers(len(current))))
        reach = closure(current)
        options = [(order[i], order[j]) for i in range(n) for j in range(i + gap, n) if not reach[i] >> j & 1]
        if options:
            current.append(options[int(rng.integers(len(options)))])
            swaps += 1
        else:
            current.append(removed)
    details['rewired_edges'] = swaps

    has_predecessor = {after for _, after in current}
    has_successor = {before for before, _ in current}
    return ([(start, t) for t in task_ids if t not in has_predecessor] + current
            + [(t, end) for t in task_ids if t not in has_successor])
