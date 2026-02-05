"""
🔴 Challenge 3A: The Multi-File App Builder
Tier: Boss Level (~20 min)

GOAL: Ask the agent to build a complete multi-file application
      with models, storage, CLI interface, and tests.

WHY THIS IS HARD:
  - Multiple files that depend on each other
  - Agent needs to plan the order of creation
  - Imports between files must be correct
  - Tests need to exercise the full stack

WHAT TO WATCH FOR:
  - Does the agent plan before coding?
  - Does it create dependencies before dependents?
  - How does it handle import paths?
  - Does it self-correct when tests fail?

HOW TO USE:
  1. Write a detailed spec (use RPI framework!)
  2. Run it and watch the agent build a real application
  3. Try using the app manually after the agent is done
"""

from agent import run_agent

if __name__ == "__main__":
    # ==========================================
    # YOUR TASK: Write the FULL spec using RPI
    # ==========================================
    # This is the boss level. Your prompt IS the spec.
    # The better your spec, the better the result.

    task = """
    Build a contact book application in the folder 'contacts/':

    FILE STRUCTURE:
    contacts/
    ├── models.py        - Contact data class
    ├── storage.py       - Save/load contacts to JSON
    ├── app.py           - CLI interface
    └── test_contacts.py - Tests for core logic

    SPECIFICATIONS:

    models.py:
    - TODO: Define the Contact class
    - TODO: What fields should a contact have?
    - TODO: Should it have a method to display itself?

    storage.py:
    - TODO: How should contacts be saved? (JSON file)
    - TODO: What functions are needed? (save, load, add, delete, search)
    - TODO: What happens if the JSON file doesn't exist yet?

    app.py:
    - TODO: What commands should the CLI support?
    - TODO: What should the user interface look like?

    test_contacts.py:
    - TODO: What should be tested?
    - TODO: How to handle test isolation (cleanup after tests)?

    After creating all files, run the tests.
    Then demonstrate the app by adding 2 contacts and listing them.

    TODO: Replace all the TODOs above with actual specifications!
    Use the RPI framework — be specific, include examples of expected behavior.
    """

    run_agent(task)
