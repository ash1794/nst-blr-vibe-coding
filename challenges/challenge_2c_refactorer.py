"""🟡 Challenge 2C: The Refactorer — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read challenges/test_files/messy.py:

1. Run it first, record exact output
2. Refactor: f→compute_signed_magnitude, g→remove_duplicates_preserve_order, h→count_vowels
   - Descriptive param names, PEP 8, type hints, Google docstrings, comments
3. Save to challenges/test_files/messy_clean.py
4. Run clean version, verify output matches original exactly"""
    run_agent(task)
