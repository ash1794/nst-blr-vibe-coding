"""🟢 Challenge 1B: The Documenter — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read challenges/test_files/hello.py and add Google-style docstrings to every function.
Each docstring: one-line summary, Args with types, Returns with type, Example with >>>.
Save to challenges/test_files/hello_documented.py. Run it to verify it still works."""
    run_agent(task)
