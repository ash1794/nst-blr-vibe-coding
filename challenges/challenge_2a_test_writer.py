"""🟡 Challenge 2A: The Test Writer — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read challenges/test_files/hello.py. Create challenges/test_files/test_hello.py:
- Use unittest, at least 3 tests per function (normal + edge + special)
- Test greet(""), farewell("World"), format_name edge cases
- Test repeat_message with times=0 (empty list) and times=1
- Run: python -m unittest challenges/test_files/test_hello.py -v
- If any fail, fix and re-run."""
    run_agent(task)
