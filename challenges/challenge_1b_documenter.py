"""
🟢 Challenge 1B: The Documenter
Tier: Warm-up (~10 min)

GOAL: Ask the agent to add professional docstrings to every function
      in a Python file.

WHAT TO WATCH FOR:
  - Does the agent read the file first to understand the functions?
  - Does it use a consistent docstring style (Google, NumPy, etc.)?
  - Does the code still work after modifications?

HOW TO USE:
  1. Look at challenges/test_files/hello.py — it has functions with no docstrings
  2. Run this script and watch the agent document them
  3. Check the output file for quality
"""

from agent import run_agent

if __name__ == "__main__":
    # ==========================================
    # YOUR TASK: Write the prompt for the agent
    # ==========================================
    # Be specific about:
    #   - Which docstring style (Google style is recommended)
    #   - What to include (description, args, returns, examples)
    #   - Whether to save to a new file or overwrite

    task = """
    TODO: Write your prompt here!
    
    The file is at: challenges/test_files/hello.py
    
    Hint: Specify the docstring format you want!
    For example, Google style looks like:
    
        def greet(name):
            \"\"\"Return a greeting message.
            
            Args:
                name: The name of the person to greet.
                
            Returns:
                A greeting string in the format "Hello, {name}!"
                
            Example:
                >>> greet("Arjun")
                'Hello, Arjun!'
            \"\"\"
    """

    run_agent(task)
