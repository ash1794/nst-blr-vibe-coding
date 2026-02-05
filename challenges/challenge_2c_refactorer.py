"""
🟡 Challenge 2C: The Refactorer
Tier: Build (~15 min)

GOAL: Give the agent a messy, unreadable Python file.
      Ask it to refactor it into clean, professional code —
      while keeping the same behavior.

WHAT TO WATCH FOR:
  - Does the agent run the original file first to capture expected outputs?
  - Does it give functions/variables meaningful names?
  - Does it verify the refactored code produces the SAME outputs?
  - Does it add docstrings and comments?

HOW TO USE:
  1. Read challenges/test_files/messy.py — it's intentionally horrible
  2. Run this script
  3. Compare the before and after
"""

from agent import run_agent

if __name__ == "__main__":
    # ==========================================
    # YOUR TASK: Write the prompt for the agent
    # ==========================================
    # The key challenge: the agent must preserve BEHAVIOR while improving STYLE.
    # This means it needs to test before AND after.

    task = """
    TODO: Write your prompt here!
    
    The file is at: challenges/test_files/messy.py
    
    Hint: A strong prompt would tell the agent to:
    1. Read the messy file
    2. Run it and SAVE the output (this is the expected behavior)
    3. Refactor with:
       - Descriptive function names (f, g, h are terrible)
       - Descriptive parameter names
       - PEP 8 formatting
       - Docstrings explaining what each function does
       - Type hints
    4. Save the refactored version to challenges/test_files/messy_clean.py
    5. Run the clean version and compare output to the original
    6. They MUST match!
    """

    run_agent(task)
