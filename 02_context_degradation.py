"""
🧞 Vibe Coding Workshop — Exercise 2: Context Degradation
Section 4: Watch the AI "Forget"

KEY INSIGHT: LLMs have a context window (like short-term memory).
When the conversation gets too long:
  - Earlier messages get pushed out
  - The AI loses track of details
  - Quality degrades, hallucinations increase

Run: python 02_context_degradation.py
"""

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
messages = []


def chat(user_message, show_tokens=True):
    """Send a message and optionally show token usage."""
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=500
    )

    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})

    if show_tokens:
        usage = response.usage
        print(f"  [TOKENS] Prompt: {usage.prompt_tokens}, "
              f"Response: {usage.completion_tokens}, "
              f"Total messages in array: {len(messages)}")

    return assistant_message


# ==========================================
# THE EXPERIMENT
# ==========================================
if __name__ == "__main__":
    print("=" * 60)
    print("  CONTEXT DEGRADATION EXPERIMENT")
    print("  Can the AI remember facts after a long conversation?")
    print("=" * 60)

    # ------------------------------------------
    # STEP 1: Give AI specific facts to remember
    # ------------------------------------------
    print("\n📝 STEP 1: Establishing facts...")
    response = chat("""
    Remember these facts about me:
    1. My name is Arjun
    2. I live in Bangalore
    3. My favorite programming language is Python
    4. My pet's name is Bruno (he's a golden retriever)
    5. I'm building a todo app for my college project
    """)
    print(f"  AI: {response[:200]}...")

    # ------------------------------------------
    # STEP 2: Quick recall test (should pass)
    # ------------------------------------------
    print("\n🧪 STEP 2: Quick recall test...")
    response = chat("What's my pet's name and what am I building?")
    print(f"  AI: {response}")

    # ------------------------------------------
    # STEP 3: Flood with filler conversations
    # ------------------------------------------
    print("\n🌊 STEP 3: Flooding with 10 filler conversations...")
    filler_topics = [
        "Explain how HTTP requests work in detail",
        "What are the differences between SQL and NoSQL databases?",
        "Explain object-oriented programming with examples",
        "What is recursion? Give me 3 examples",
        "Explain the concept of REST APIs",
        "What are the main design patterns in software engineering?",
        "Explain Git version control and branching strategies",
        "What is cloud computing and how does AWS work?",
        "Explain Docker containers and how they differ from VMs",
        "What are microservices and when should you use them?"
    ]

    for i, topic in enumerate(filler_topics):
        print(f"  Filler {i + 1}/10: {topic[:50]}...")
        chat(topic, show_tokens=True)

    # ------------------------------------------
    # STEP 4: Test recall again (will it remember?)
    # ------------------------------------------
    print("\n" + "=" * 60)
    print("🧪 STEP 4: Final recall test — does it still remember?")
    print("=" * 60)
    response = chat(
        "Quick question — what's my name, where do I live, "
        "what's my pet's name, and what am I building?"
    )
    print(f"\n  AI: {response}")

    # ------------------------------------------
    # RESULTS
    # ------------------------------------------
    print("\n" + "=" * 60)
    print("📊 RESULTS")
    print("=" * 60)
    print(f"  Total messages in array: {len(messages)}")
    print()
    print("  EXPECTED FACTS:")
    print("    Name: Arjun")
    print("    City: Bangalore")
    print("    Pet:  Bruno (golden retriever)")
    print("    Project: Todo app")
    print()
    print("  ❓ Did the AI get all 4 correct?")
    print("  ❓ Did it hallucinate any details?")
    print("  ❓ What does this mean for long coding sessions?")
    print()
    print("  💡 LESSON: Context has limits.")
    print("     Keep conversations focused. Start fresh for new tasks.")
    print("=" * 60)
