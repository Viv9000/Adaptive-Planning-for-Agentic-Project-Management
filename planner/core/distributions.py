"""Task duration distributions: PERT for tasks and tabular for the zero-duration milestones; validation, sampling,
and content hashing."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
import hashlib
import json
import math
from numbers import Integral, Real
from types import MappingProxyType
from typing import Any, Literal, TypeAlias

from numpy.random import Generator
from scipy import stats


DurationProbabilities: TypeAlias = Mapping[int, float]
DistributionFamily: TypeAlias = Literal["pert", "tabular"]

PROBABILITY_TOLERANCE = 1e-12

# Parameter names per family; tabular distributions use probabilities instead.
REQUIRED_PARAMETERS = {
    "pert": {"a", "b", "c"},  # minimum, mode, maximum
    "tabular": set(),  # {day: probability}
}


@dataclass(frozen=True, slots=True)
class DurationDistribution:
    """Read-only raw duration distribution X; the MDP rounds samples to D = ceil(max(0, X))."""

    family: DistributionFamily
    parameters: Mapping[str, float] = field(default_factory=dict)
    probabilities: DurationProbabilities = field(default_factory=dict)

    _scipy_distribution: Any = field(init=False, default=None, repr=False, compare=False)
    # Search asks for the same CDF and survival points many times; SciPy is slow, so continuous families cache them.
    _point_cache: Any = field(init=False, default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        """Copy the inputs into read-only mappings, then validate."""
        object.__setattr__(self, "parameters", MappingProxyType(dict(self.parameters)))
        object.__setattr__(self, "probabilities", MappingProxyType(dict(self.probabilities)))
        self.validate()

    def validate(self) -> None:
        """Raise ValueError for an invalid specification.

        Checks: known family, exactly its parameter names, finite numbers,
        a nonempty tabular table of nonnegative integer days with probabilities summing to one,
        and 0 <= a < b < c for PERT.
        """
        def reject(reason: str) -> None:
            raise ValueError(f"{self.family} distribution: {reason}")

        # Check the family and its parameter names and values
        if self.family not in REQUIRED_PARAMETERS:
            reject("unknown family, must be one of: " + ", ".join(sorted(REQUIRED_PARAMETERS)))
        expected_fields = REQUIRED_PARAMETERS[self.family]
        if set(self.parameters) != expected_fields:
            reject(f"parameters must contain exactly {sorted(expected_fields)}")
        for name, value in self.parameters.items():
            if not isinstance(value, Real) or not math.isfinite(value):
                reject(f"{name} must be finite numeric data")

        # Check the table: nonnegative integer days with probabilities summing to one
        if self.family == "tabular":
            if not self.probabilities:
                reject("probabilities must be nonempty")
            for day, probability in self.probabilities.items():
                if not isinstance(day, Integral) or day < 0:
                    reject(f"duration {day!r} must be a nonnegative integer")
                if not isinstance(probability, Real) or not math.isfinite(probability) or probability < 0:
                    reject(f"probability at duration {day} must be finite and nonnegative")
            if abs(math.fsum(self.probabilities.values()) - 1) > PROBABILITY_TOLERANCE:
                reject(f"probabilities must sum to one within {PROBABILITY_TOLERANCE}")
        elif self.probabilities:
            reject("probabilities are only allowed for tabular distributions")

        # Check the parameter ordering of each family
        parameters = self.parameters
        if self.family == "pert" and not 0 <= parameters["a"] < parameters["b"] < parameters["c"]:
            reject("a, b, c must satisfy 0 <= a < b < c")

    def _prepared_distribution(self) -> Any:
        """Build the SciPy distribution once and reuse it."""
        if self._scipy_distribution is None:
            object.__setattr__(self, "_scipy_distribution", self._create_scipy_distribution())
        return self._scipy_distribution

    def _create_scipy_distribution(self) -> Any:
        """Return the frozen SciPy distribution of a PERT duration."""
        # Minimum a, mode b, maximum c, with the mode as a fraction of the width
        parameters = self.parameters
        width = parameters["c"] - parameters["a"]
        fraction = (parameters["b"] - parameters["a"]) / width
        # Standard beta-PERT uses shape weight four.
        alpha = 1 + 4 * fraction
        beta = 1 + 4 * (1 - fraction)
        return stats.beta(alpha, beta, loc=parameters["a"], scale=width)

    def evaluate_cdf(self, x: float) -> float:
        """Return Pr(X <= x)."""
        if self.family == "tabular":
            return math.fsum(probability for day, probability in self.probabilities.items() if day <= x)
        return self._cached('cdf', x)

    def survival(self, x: float) -> float:
        """Return Pr(X > x), computed directly rather than as 1 - CDF."""
        if self.family == "tabular":
            return math.fsum(probability for day, probability in self.probabilities.items() if day > x)
        return self._cached('sf', x)

    def log_survival(self, x: float) -> float:
        """Return log Pr(X > x), which keeps tiny tails that would underflow to zero."""
        if self.family == "tabular":
            survival = self.survival(x)
            return math.log(survival) if survival > 0 else -math.inf
        return self._cached('logsf', x)

    def _cached(self, function: str, x: float) -> float:
        """Return the SciPy function's value at x, computing each (function, x) once."""
        if self._point_cache is None:
            object.__setattr__(self, "_point_cache", {})
        key = (function, x)
        value = self._point_cache.get(key)
        if value is None:
            value = float(getattr(self._prepared_distribution(), function)(x))
            self._point_cache[key] = value
        return value

    def sample(self, rng: Generator) -> float:
        """Sample raw X; the MDP rounds it up to whole time units."""
        if self.family == "tabular":
            return self._sample_table(self.probabilities, rng)
        return float(self._prepared_distribution().rvs(random_state=rng))

    @staticmethod
    def _sample_table(probabilities: DurationProbabilities, rng: Generator, *, total: float = 1.0) -> float:
        """Sample a duration table; total is the remaining mass when conditioning."""
        # Walk the table in day order until the cumulative mass passes a uniform draw
        threshold = float(rng.random()) * total
        cumulative = 0.0
        last_day = 0
        for day, probability in sorted(probabilities.items()):
            if probability == 0:
                continue
            last_day = day
            cumulative += probability
            if threshold < cumulative:
                return float(day)
        # Rounding can leave the threshold just above the total; use the last positive day.
        return float(last_day)

    def sample_above(self, lower: float, rng: Generator) -> float:
        """Sample X conditional on X > lower, without rejection sampling in small tails."""
        if math.isnan(lower):
            raise ValueError("Conditional lower bound must not be NaN")
        if lower == -math.inf:
            return self.sample(rng)

        # Tabular: sample from the days above the bound, renormalized
        if self.family == "tabular":
            remaining = {day: p for day, p in self.probabilities.items() if day > lower and p > 0}
            survival = math.fsum(remaining.values())
            if survival == 0:
                raise ValueError("tabular distribution: empty support above lower bound")
            return self._sample_table(remaining, rng, total=survival)

        # PERT: sample the tail above the bound directly
        distribution = self._prepared_distribution()
        if lower >= distribution.support()[1]:
            raise ValueError(f"{self.family} distribution: empty support above lower bound")
        # Invert the survival function to avoid subtracting a near-one CDF.
        survival = float(distribution.sf(lower))
        if survival == 0:
            raise FloatingPointError(f"{self.family}: conditional survival underflow")
        result = float(distribution.isf((1 - float(rng.random())) * survival))
        if not math.isfinite(result) or result <= lower:
            raise FloatingPointError(f"{self.family}: cannot represent conditional sample above {lower}")
        return result

    def mean(self) -> float:
        """Return the raw mean E[X]."""
        if self.family == "tabular":
            return math.fsum(day * probability for day, probability in self.probabilities.items())
        return float(self._prepared_distribution().mean())


def distribution_key(distribution: DurationDistribution) -> str:
    """Return the SHA-256 hash of the specification, independent of mapping order."""
    specification = {
        "family": distribution.family,
        "parameters": {name: float(value) for name, value in distribution.parameters.items()},
        "probabilities": [[int(day), float(p)] for day, p in sorted(distribution.probabilities.items())],
    }
    encoded = json.dumps(specification, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def register_distribution(distributions: dict[str, DurationDistribution], distribution: DurationDistribution) -> str:
    """Add a distribution to a project table (keeping the first equal entry) and return its key."""
    key = distribution_key(distribution)
    distributions.setdefault(key, distribution)
    return key


def expected_duration(distribution: DurationDistribution) -> float:
    """Return E[D] for the rounded duration D = ceil(max(0, X)), as the sum of Pr(X > day)."""
    if distribution.family == 'tabular':
        return distribution.mean()

    # E[D] = sum over days d >= 0 of Pr(X > d), summed until the terms vanish
    def survival_terms():
        """Pr(X > 0), Pr(X > 1), ..., ending at the first zero term (past the PERT maximum)."""
        day = 0
        while True:
            survival = distribution.survival(day)
            yield survival
            if survival == 0:
                return
            day += 1

    return math.fsum(survival_terms())


def duration_bounds(distribution: DurationDistribution) -> tuple[int, int | float]:
    """Return the shortest and longest possible rounded duration."""
    # A table is bounded by its days with positive probability
    if distribution.family == "tabular":
        days = [day for day, probability in distribution.probabilities.items() if probability > 0]
        return min(days), max(days)

    # PERT is bounded by its minimum and maximum; it puts no mass on the minimum itself, so a = 1 rounds to at least 2
    parameters = distribution.parameters
    return math.floor(parameters["a"]) + 1, math.ceil(parameters["c"])
