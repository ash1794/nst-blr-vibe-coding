"""
🧞 Vibe Coding Workshop — Setup Test
Run this BEFORE the workshop to make sure everything works.

Usage: python 00_setup_test.py
"""

import sys

# ==========================================
# CHECK 1: Python version
# ==========================================
print("Checking Python version...", end=" ")
if sys.version_info < (3, 8):
    print(f"❌ Python 3.8+ required, you have {sys.version}")
    sys.exit(1)
print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")

# ==========================================
# CHECK 2: Required packages
# ==========================================
print("Checking packages...", end=" ")
try:
    from groq import Groq
    from dotenv import load_dotenv
    print("✅ groq and python-dotenv installed")
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("   Run: pip install groq python-dotenv")
    sys.exit(1)

# ==========================================
# CHECK 3: .env file exists
# ==========================================
import os
print("Checking .env file...", end=" ")
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key or api_key == "your_key_here":
    print("❌ No API key found")
    print("   1. Copy .env.example to .env")
    print("   2. Get a free key at https://console.groq.com")
    print("   3. Paste it in your .env file")
    sys.exit(1)
print("✅ API key found")

# ==========================================
# CHECK 4: API key actually works
# ==========================================
print("Testing API connection...", end=" ")
try:
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": "Say 'hello' and nothing else."}],
        max_tokens=10
    )
    reply = response.choices[0].message.content.strip()
    print(f"✅ Got response: \"{reply}\"")
except Exception as e:
    print(f"❌ API call failed: {e}")
    print("   Check your API key at https://console.groq.com")
    sys.exit(1)

# ==========================================
# ALL GOOD
# ==========================================
print()
print("=" * 50)
print("✅ Setup complete! You're ready for the workshop.")
print("=" * 50)
