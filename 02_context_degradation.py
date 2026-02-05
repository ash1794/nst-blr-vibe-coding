"""
🧞 Vibe Coding Workshop — Exercise 2: Context Degradation
Section 4: Watch the AI "Forget"

KEY INSIGHT: LLMs have a context window (like short-term memory).
When the conversation gets too long, or when you limit context,
the AI loses track of earlier details.

This demo has TWO parts:
  Part A: Natural experiment (may still remember with large context windows)
  Part B: Simulated small context window — THIS is where it breaks

Run: python 02_context_degradation.py
"""

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = []


def chat(user_message, show_tokens=True):
    """Send a message using the full conversation history."""
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
              f"Total messages: {len(messages)}")

    return assistant_message


def chat_with_window(user_message, window_size):
    """Send a message but only include the last `window_size` messages.

    This simulates what happens when context is limited —
    like a model with a tiny context window, or when an app
    truncates history to save costs.
    """
    messages.append({"role": "user", "content": user_message})

    # Only send the last N messages
    windowed_messages = messages[-window_size:]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=windowed_messages,
        max_tokens=500
    )

    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})

    usage = response.usage
    print(f"  [TOKENS] Prompt: {usage.prompt_tokens} "
          f"(sent {len(windowed_messages)} of {len(messages)} total messages)")

    return assistant_message


# ==========================================
# PART A: FULL CONTEXT — DOES IT REMEMBER?
# ==========================================

print("=" * 60)
print("  CONTEXT DEGRADATION EXPERIMENT")
print("=" * 60)

# Step 1: Establish facts
print("\n📝 STEP 1: Establishing facts...")
response = chat("""
Remember these facts about me:
1. My name is Arjun
2. I live in Bangalore
3. My favorite programming language is Python
4. My pet's name is Bruno (he's a golden retriever)
5. I'm building a todo app for my college project
6. My student ID is NST-2024-0742
7. I prefer dark mode in all my editors
""")
print(f"  AI: {response[:200]}...")

# Step 2: Quick recall
print("\n🧪 STEP 2: Quick recall test...")
response = chat("What's my student ID and my pet's name?")
print(f"  AI: {response}")

# Step 3: Flood with filler
print("\n🌊 STEP 3: Flooding with 10 filler conversations...")
filler_topics = [
    "Explain how HTTP requests work. Cover GET, POST, PUT, DELETE, headers, status codes, and the full request/response cycle in detail.",
    "Compare SQL vs NoSQL databases. Cover PostgreSQL, MongoDB, Redis, Cassandra with detailed use cases for each.",
    "Explain OOP with detailed Python examples. Cover classes, inheritance, polymorphism, encapsulation, abstract classes.",
    "What is recursion? Give 5 examples: fibonacci, tree traversal, tower of hanoi, binary search, merge sort. Show code.",
    "Explain REST APIs in detail: HTTP methods, status codes, OAuth, JWT authentication, rate limiting, API versioning.",
    "Describe design patterns: Singleton, Factory, Observer, Strategy, Decorator. Show Python implementations of each.",
    "Explain Git comprehensively: branching, merging, rebasing, cherry-picking, conflict resolution, Git flow.",
    "What is cloud computing? Explain IaaS, PaaS, SaaS, serverless, containers. Compare AWS, GCP, Azure services.",
    "Explain Docker: Dockerfiles, images, containers, volumes, networks, docker-compose, multi-stage builds.",
    "What are microservices? Architecture, service discovery, API gateways, event-driven communication, saga pattern.",
]

for i, topic in enumerate(filler_topics):
    print(f"  Filler {i + 1}/10: {topic[:50]}...")
    chat(topic, show_tokens=True)

# Step 4: Recall with full context
print("\n" + "=" * 60)
print("🧪 PART A: Full context recall test")
print("=" * 60)
response = chat(
    "Quick — what's my name, student ID, pet's name, and "
    "what project am I building?"
)
print(f"\n  AI: {response}")
print(f"\n  💡 The model has a 128K token context window.")
print(f"     We only used ~{len(messages) * 300} tokens — it probably remembered fine!")

# ==========================================
# PART B: SMALL CONTEXT WINDOW SIMULATION
# ==========================================

print("\n\n" + "=" * 60)
print("  PART B: WHAT IF THE CONTEXT WINDOW WAS TINY?")
print("  Simulating: only send the last 4 messages to the AI")
print("=" * 60)

print("\n🔬 Same question, but the AI can only see the last 4 messages...")
print("   (The facts were established 20+ messages ago — now invisible)\n")

response = chat_with_window(
    "Quick — what's my name, student ID, pet's name, and "
    "what project am I building?",
    window_size=4
)
print(f"\n  AI: {response}")

print("\n" + "-" * 60)
print("🔬 Even smaller: only the last 2 messages (just this question)...\n")

response = chat_with_window(
    "What is my name and where do I live?",
    window_size=2
)
print(f"\n  AI: {response}")

# ==========================================
# THE LESSON
# ==========================================
print("\n" + "=" * 60)
print("📊 WHAT JUST HAPPENED")
print("=" * 60)
print("""
  PART A (all messages sent):    Probably remembered everything ✅
  PART B (last 4 messages):      Lost the original facts ❌
  PART B (last 2 messages):      Completely clueless ❌

  WHY THIS MATTERS FOR YOU:
  ─────────────────────────
  1. ChatGPT, Claude, Cursor — they manage context FOR you.
     Behind the scenes, they summarize or drop old messages
     when conversations get long. You've probably noticed
     ChatGPT "forgetting" things in long chats — this is why.

  2. When YOU build an agent (like we will in 30 minutes),
     YOU manage the messages array. If it gets too long:
     → API costs increase (you pay per token)
     → Old context gets less "attention" from the model
     → Eventually you MUST truncate or summarize

  3. PRACTICAL RULES:
     → Start fresh conversations for new tasks
     → Don't do everything in one mega-conversation
     → Keep prompts focused and specific (RPI framework!)
     → When building agents, monitor your context size
""")
print("=" * 60)
