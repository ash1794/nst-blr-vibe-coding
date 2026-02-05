"""
🧞 Vibe Coding Workshop — Exercise 1: Basic Chat
Section 3: The Mental Model

KEY INSIGHT: The LLM is STATELESS.
- It doesn't "remember" anything.
- YOU manage the conversation as a Python list.
- Every API call sends the ENTIRE conversation history.

Run: python 01_basic_chat.py
"""

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ==========================================
# THE CONVERSATION IS JUST AN ARRAY
# ==========================================
# This is the entire "memory" of the conversation.
# There's no magic. It's a list of dictionaries.
messages = []


def chat(user_message):
    """Send a message and get a response.
    
    Watch what happens to the messages array after each call.
    """
    # Step 1: Add user message to array
    messages.append({
        "role": "user",
        "content": user_message
    })

    # Step 2: Send ENTIRE array to AI
    # Every single previous message gets sent every time!
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        max_tokens=500
    )

    # Step 3: Get the AI's response
    assistant_message = response.choices[0].message.content

    # Step 4: Add AI response to array (so it's included next time)
    messages.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


# ==========================================
# RUN THE CHAT
# ==========================================
if __name__ == "__main__":
    print("🤖 Chat started. Type 'quit' to exit.")
    print("   Watch the message count grow after each turn!\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        response = chat(user_input)
        print(f"\nAI: {response}\n")

        # REVEAL THE MAGIC: Show the growing array
        print(f"[DEBUG] Messages array now has {len(messages)} items")
        print(f"[DEBUG] Roles: {[m['role'] for m in messages]}\n")

    # ==========================================
    # AFTER QUITTING: Inspect the full array
    # ==========================================
    print("\n" + "=" * 50)
    print("FULL CONVERSATION ARRAY:")
    print("=" * 50)
    for i, msg in enumerate(messages):
        role = msg["role"].upper()
        content = msg["content"][:80] + "..." if len(msg["content"]) > 80 else msg["content"]
        print(f"  [{i}] {role}: {content}")

    print(f"\nTotal messages: {len(messages)}")
    print("This ENTIRE array was sent with every single API call.")
