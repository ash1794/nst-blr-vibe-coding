"""
🟢 Challenge 1A: The Bug Fixer
Tier: Warm-up (~10 min)

GOAL: Give the agent a file full of bugs. Watch it find and fix them.

WHAT TO WATCH FOR:
  - Does the agent RUN the file first to see the errors?
  - Does it fix all the bugs or just the first one?
  - Does it TEST after fixing?

HOW TO USE:
  1. Read the buggy file first (challenges/test_files/buggy.py) to understand the bugs
  2. Run this script and watch the agent work
  3. Check if the agent caught all 4 bugs

BUGS IN THE FILE:
  1. calculate_average crashes on empty list (ZeroDivisionError)
  2. find_max returns 0 for all-negative lists
  3. reverse_string has an off-by-one index error
  4. count_words miscounts when there are multiple spaces
"""

from agent import run_agent

if __name__ == "__main__":
    # ==========================================
    # YOUR TASK: Write the prompt for the agent
    # ==========================================
    # Replace the prompt below. Be specific! (Remember the genie lesson)
    # Hint: Tell the agent to run the file first, then fix, then verify.

    task = """
    TODO: Write your prompt here!
    
    The file is at: challenges/test_files/buggy.py
    
    Hint: A good prompt would tell the agent to:
    1. Read the file
    2. Run it to see what errors occur
    3. Fix ALL the bugs
    4. Run it again to verify all tests pass
    """

    run_agent(task)
