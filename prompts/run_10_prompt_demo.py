"""
🧞 Vibe Coding Workshop — 10-Prompt Live Demo Runner
Section 2: Prompt Engineering Crash Course

USE THIS during the workshop to run the 10-prompt challenge live.
It sends each prompt to the LLM and shows the response side-by-side
so students can see how quality improves with prompt specificity.

Usage:
  python prompts/run_10_prompt_demo.py          # Run all 10 levels
  python prompts/run_10_prompt_demo.py 1 4 7 10 # Run specific levels only
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from groq import Groq
from dotenv import load_dotenv
from prompts.all_prompts import (
    LEVEL_01, LEVEL_02, LEVEL_03, LEVEL_04, LEVEL_05,
    LEVEL_06, LEVEL_07, LEVEL_08, LEVEL_09, LEVEL_10,
)

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

LEVELS = {
    1:  ("The 'I wish for stuff' prompt", LEVEL_01),
    2:  ("Slightly better", LEVEL_02),
    3:  ("Adds language", LEVEL_03),
    4:  ("Adds criteria", LEVEL_04),
    5:  ("Adds thresholds", LEVEL_05),
    6:  ("Better return type", LEVEL_06),
    7:  ("Adds edge cases", LEVEL_07),
    8:  ("Adds examples (one-shot)", LEVEL_08),
    9:  ("Adds test cases", LEVEL_09),
    10: ("The Full Genie-Proof Spec", LEVEL_10),
}


def run_level(level_num):
    """Run a single prompt level and display the result."""
    title, prompt = LEVELS[level_num]

    print(f"\n{'=' * 70}")
    print(f"  LEVEL {level_num}/10: {title}")
    print(f"{'=' * 70}")

    # Show the prompt (truncated if long)
    display_prompt = prompt.strip()
    if len(display_prompt) > 200:
        display_prompt = display_prompt[:200] + "\n  [...truncated — see all_prompts.py for full text]"
    print(f"\n📝 PROMPT:\n{display_prompt}")

    print(f"\n{'─' * 70}")
    print("🤖 RESPONSE:")
    print(f"{'─' * 70}\n")

    # Send to LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )

    reply = response.choices[0].message.content
    print(reply)

    # Show token usage
    usage = response.usage
    print(f"\n[TOKENS] Prompt: {usage.prompt_tokens}, Response: {usage.completion_tokens}")

    print(f"\n{'=' * 70}")
    input("Press Enter for next level...")


def main():
    # Parse which levels to run
    if len(sys.argv) > 1:
        levels_to_run = [int(x) for x in sys.argv[1:]]
    else:
        levels_to_run = list(range(1, 11))

    print("🧞 THE 10-PROMPT CHALLENGE")
    print("   Same task: Password Strength Checker")
    print("   Watch how output quality transforms with prompt quality.\n")
    print(f"   Running levels: {levels_to_run}")
    input("\nPress Enter to start...")

    for level in levels_to_run:
        if level in LEVELS:
            run_level(level)
        else:
            print(f"⚠️ Level {level} doesn't exist (valid: 1-10)")

    print("\n" + "=" * 70)
    print("  🎯 THE PUNCHLINE")
    print("=" * 70)
    print("""
  Level 1  → "I wish for stuff"        → Garbage
  Level 5  → "I wish for this stuff"   → Decent
  Level 10 → Genie-proof spec          → Exactly right

  The effort you put into the PROMPT
  determines the quality of the OUTPUT.

  Prompting isn't "talking to AI."
  Prompting is ENGINEERING.
""")


if __name__ == "__main__":
    main()
