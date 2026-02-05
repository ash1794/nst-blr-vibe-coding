"""🟢 Challenge 1A: The Bug Fixer — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read the file challenges/test_files/buggy.py and do the following:

1. First, run it with: python challenges/test_files/buggy.py
2. Observe all errors and incorrect outputs
3. Fix ALL bugs:
   - calculate_average crashes on empty list — return 0 for empty
   - find_max returns wrong result for all-negative lists — don't initialize to 0
   - reverse_string has an off-by-one index error in range
   - count_words miscounts with multiple spaces — use split() not split(" ")
4. After fixing, run it again
5. Verify: Test 1: 20.0, Test 2: 0, Test 3: -2, Test 4: olleh, Test 5: 2"""
    run_agent(task)
