"""The LLM-based method (entry: llm_run.py, the stages): prompts (prompts/), generation through the OpenAI
or Amazon Bedrock API (generation.py, settings.py), the observation given to a policy (observation.py), and the
player: each policy in its own process, with greedy as fallback (player.py, policy_process.py, policy_worker.py).
"""
