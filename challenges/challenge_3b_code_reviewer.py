"""🔴 Challenge 3B: Code Reviewer — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read 03_simple_agent.py. Write review_notes.md (Category/Severity/Description/Fix).

Check: run_command security (High), invalid JSON from tool args (Medium), no retries (Medium),
max_tokens truncation (Low), magic strings (Low), no logging (Medium).

Create 03_simple_agent_v2.py with top 5 fixes: BLOCKED_COMMANDS, try/except JSON,
retry logic (2 retries, 1s delay), constant for model name, timestamped logging.
Test v2: create and run test_v2.py that prints 'v2 works!'"""
    run_agent(task)
