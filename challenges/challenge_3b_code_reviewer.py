"""
🔴 Challenge 3B: The Code Reviewer
Tier: Boss Level (~20 min)

GOAL: Ask the agent to review its OWN agent code (03_simple_agent.py),
      suggest improvements, implement them, and verify the improved
      version still works.

WHY THIS IS MIND-BENDING:
  - The agent is reading and improving the code that MAKES agents
  - It's using the tool loop to improve the tool loop
  - Meta-programming in action

WHAT TO WATCH FOR:
  - What improvements does the AI suggest?
  - Does it find real issues or just cosmetic ones?
  - Does the improved version actually work?
  - How does it test the new version?

HOW TO USE:
  1. Run this script
  2. Read the agent's review carefully
  3. Compare the original and improved versions
  4. Do YOU agree with the improvements?
"""

from agent import run_agent

if __name__ == "__main__":
    # ==========================================
    # YOUR TASK: Write the prompt
    # ==========================================
    # Guide the agent to do a structured code review.

    task = """
    TODO: Write your prompt here!
    
    The agent code is at: 03_simple_agent.py
    
    Hint: Ask the agent to:
    1. Read 03_simple_agent.py
    2. Analyze it for:
       - Potential bugs or edge cases not handled
       - Security concerns (hint: run_command is dangerous!)
       - Code organization improvements
       - Error handling gaps
       - Missing features that would make it more robust
    3. List the top 3-5 improvements with explanations
    4. Create an improved version as 03_simple_agent_v2.py
    5. Test the new version with a simple task
    
    BONUS: Can you think of improvements the agent might miss?
    What about:
    - What if a tool call returns invalid JSON?
    - What if the LLM hallucinates a tool name?
    - What if run_command is used to delete files?
    - What about rate limiting?
    """

    run_agent(task)
