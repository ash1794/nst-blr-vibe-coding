"""
🟡 Challenge 2B: The Project Scaffolder
Tier: Build (~15 min)

GOAL: Ask the agent to create an entire project from scratch —
      multiple files, tests, documentation.

WHAT TO WATCH FOR:
  - How does the agent plan the project structure?
  - Does it create files in the right order (dependencies first)?
  - Does it run the tests at the end?
  - How many iterations does it take?

HOW TO USE:
  1. Run this script
  2. Watch the agent create a mini-project from nothing
  3. Inspect the generated files
"""

from agent import run_agent

if __name__ == "__main__":
    # ==========================================
    # YOUR TASK: Write the prompt for the agent
    # ==========================================
    # The prompt below is partially written. Finish it!
    # Be specific about what each file should contain.

    task = """
    Create a Python calculator project in the folder 'my_calculator/' with these files:

    1. my_calculator/calculator.py
       - A Calculator class with methods: add, subtract, multiply, divide
       - TODO: What should divide do when dividing by zero?
       - TODO: What types should the methods accept?

    2. my_calculator/test_calculator.py
       - Unit tests using unittest
       - TODO: How many tests per method?
       - TODO: What edge cases should be tested?

    3. my_calculator/README.md
       - Brief description and usage examples

    After creating everything, run the tests.

    TODO: Finish this prompt! Add the missing specifications.
    """

    run_agent(task)
