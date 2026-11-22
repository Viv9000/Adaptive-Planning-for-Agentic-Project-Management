# LLM-based method

A large language model writes a scheduling policy as a Python function, from the prompts in `prompts/`: a general
policy per instance set (S, L) or an instance-specific one. Each policy then runs in its own process, with 60 s to
build and 1 s per decision; if it fails at a decision, the greedy method decides instead. The process is not a
sandbox: generated code runs with your permissions, so read the programs in `results/llm/programs/` before evaluating them.

    python -m planner.methods.llm.llm_run --stage prepare       # prompts, no API calls
    python -m planner.methods.llm.llm_run --stage generate --models sol --execute-paid --api-cap 100 --max-hours 4
    python -m planner.methods.llm.llm_run --stage evaluate --models sol --parallel 8
    python -m planner.methods.llm.llm_run --stage report

Sol, Luna and Astra use the OpenAI API (`OPENAI_API_KEY`); DeepSeek V3.2 and Kimi K3.1 use Amazon Bedrock (`boto3` and
AWS credentials). Generation stops at the dollar cap. New generations give new policies, so results differ from the
paper's.
