"""
🟡 Challenge 2A: The Test Writer
Tier: Build (~15 min)

GOAL: Ask the agent to read a file, write unit tests for it,
      and run them — fixing any failures.

THE MAGIC MOMENT: The agent writes tests, runs them, some fail,
and the agent fixes them. Self-correcting loop in action!

WHAT TO WATCH FOR:
  - Does the agent read the source file to understand the functions?
  - Does it generate meaningful test cases (not just trivial ones)?
  - When a test fails, does the agent figure out why and fix it?
  - Does it test edge cases?

HOW TO USE:
  1. Look at challenges/test_files/hello.py to know what functions exist
  2. Run this script
  3. Watch the agent write tests, run them, and self-correct
"""

from agent import run_agent

if __name__ == "__main__":
    # ==========================================
    # YOUR TASK: Write the prompt for the agent
    # ==========================================
    # Think about:
    #   - Which testing framework? (unittest is built-in, no pip install needed)
    #   - How many tests per function?
    #   - Should it test edge cases?
    #   - What should happen after writing tests?

    task = """
    TODO: Write your prompt here!
    
    The file is at: challenges/test_files/hello.py
    
    Hint: A good prompt would specify:
    - Read the source file first
    - Use Python's unittest module (no external deps)
    - Write at least 2 tests per function (normal case + edge case)
    - Save tests to challenges/test_files/test_hello.py
    - Run the tests
    - If any fail, fix them and re-run
    """

    run_agent(task)
