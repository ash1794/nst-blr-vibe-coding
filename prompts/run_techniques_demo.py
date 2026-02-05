"""
🧞 Vibe Coding Workshop — 5 Techniques Live Demo
Section 2: Prompt Engineering Crash Course

Run bad vs good prompts side-by-side so students can see the difference.

Usage:
  python prompts/run_techniques_demo.py       # Run all 5
  python prompts/run_techniques_demo.py 1 2   # Run specific ones
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from groq import Groq
from dotenv import load_dotenv
from prompts.all_prompts import (
    TECHNIQUE_1_BAD, TECHNIQUE_1_GOOD,
    TECHNIQUE_2_BAD, TECHNIQUE_2_GOOD,
    TECHNIQUE_3_BAD, TECHNIQUE_3_GOOD,
    TECHNIQUE_4_BAD, TECHNIQUE_4_GOOD,
    TECHNIQUE_5_BAD, TECHNIQUE_5_GOOD,
)

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

TECHNIQUES = {
    1: ("Be Painfully Specific", TECHNIQUE_1_BAD, TECHNIQUE_1_GOOD),
    2: ("One-Shot Prompting", TECHNIQUE_2_BAD, TECHNIQUE_2_GOOD),
    3: ("Define Output Format", TECHNIQUE_3_BAD, TECHNIQUE_3_GOOD),
    4: ("Set Constraints", TECHNIQUE_4_BAD, TECHNIQUE_4_GOOD),
    5: ("Chain of Thought", TECHNIQUE_5_BAD, TECHNIQUE_5_GOOD),
}


def send_prompt(prompt):
    """Send a prompt and return the response text."""
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    return response.choices[0].message.content


def run_technique(num):
    """Run bad vs good comparison for one technique."""
    name, bad, good = TECHNIQUES[num]

    print(f"\n{'=' * 70}")
    print(f"  TECHNIQUE {num}: {name}")
    print(f"{'=' * 70}")

    # --- BAD PROMPT ---
    print(f"\n❌ BAD PROMPT: \"{bad}\"")
    print(f"{'─' * 70}")
    bad_response = send_prompt(bad)
    # Truncate long responses for demo
    if len(bad_response) > 500:
        bad_response = bad_response[:500] + "\n  [...truncated]"
    print(bad_response)

    print(f"\n{'─' * 70}")

    # --- GOOD PROMPT ---
    display_good = good.strip()
    if len(display_good) > 300:
        display_good = display_good[:300] + "\n  [...see all_prompts.py]"
    print(f"\n✅ GOOD PROMPT:\n{display_good}")
    print(f"{'─' * 70}")
    good_response = send_prompt(good)
    if len(good_response) > 500:
        good_response = good_response[:500] + "\n  [...truncated]"
    print(good_response)

    print(f"\n💡 Notice the difference? The good prompt left no room for the genie.")
    input("\nPress Enter for next technique...")


def main():
    if len(sys.argv) > 1:
        to_run = [int(x) for x in sys.argv[1:]]
    else:
        to_run = list(range(1, 6))

    print("🧞 THE 5 PROMPT ENGINEERING TECHNIQUES")
    print("   Bad prompt vs Good prompt — side by side.\n")
    print(f"   Running techniques: {to_run}")
    input("\nPress Enter to start...")

    for num in to_run:
        if num in TECHNIQUES:
            run_technique(num)
        else:
            print(f"⚠️ Technique {num} doesn't exist (valid: 1-5)")

    print("\n✅ Done! These 5 techniques cover 90% of prompt engineering.")


if __name__ == "__main__":
    main()
