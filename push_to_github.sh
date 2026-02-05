#!/bin/bash
# ==========================================
# Run this script AFTER unzipping the repo
# It sets up all branches and pushes to GitHub
# ==========================================

set -e

REPO_URL="git@github.com:ash1794/nst-blr-vibe-coding.git"

echo "🚀 Setting up vibe-coding-workshop repo..."
echo ""

# cd vibe-coding-workshop

# Init and configure
git init
git branch -m main
git remote add origin "$REPO_URL"

# ==========================================
# BRANCH: main (setup only)
# ==========================================
echo "📦 Branch: main"
git add README.md requirements.txt .env.example .gitignore 00_setup_test.py
git commit -m "Initial setup: README, requirements, and setup test

Students start here. Run 00_setup_test.py to verify API key works."

# ==========================================
# BRANCH: 01-basic-chat
# ==========================================
echo "📦 Branch: 01-basic-chat"
git checkout -b 01-basic-chat
git add 01_basic_chat.py
git commit -m "Section 3: Basic Chat — LLMs are stateless

The conversation is just a Python list. Every API call sends the ENTIRE array.
Usage: python 01_basic_chat.py"

# ==========================================
# BRANCH: 02-context-degradation
# ==========================================
echo "📦 Branch: 02-context-degradation"
git checkout -b 02-context-degradation
git add 02_context_degradation.py
git commit -m "Section 4: Context Degradation — Watch the AI forget

Floods conversation with filler, tests if AI still recalls earlier facts.
Usage: python 02_context_degradation.py"

# ==========================================
# BRANCH: 03-simple-agent
# ==========================================
echo "📦 Branch: 03-simple-agent"
git checkout -b 03-simple-agent
git add 03_simple_agent.py
git commit -m "Section 6: Build Your Agent — The agent loop (code-along)

An agent = LLM + tools + while loop. 4 primitives: list, read, write, run.
Usage: python 03_simple_agent.py"

# ==========================================
# BRANCH: 04-challenges
# ==========================================
echo "📦 Branch: 04-challenges"
git checkout -b 04-challenges
git add challenges/
git commit -m "Section 7: Agent Challenges — You code!

🟢 Tier 1: Bug Fixer, Documenter
🟡 Tier 2: Test Writer, Scaffolder, Refactorer
🔴 Tier 3: Multi-File App, Code Reviewer

Each has a TODO prompt — students write their own using prompt eng techniques."

# ==========================================
# BRANCH: 05-prompts
# ==========================================
echo "📦 Branch: 05-prompts"
git checkout -b 05-prompts
git add prompts/
git commit -m "Section 2: All workshop prompts + live demo runners

- all_prompts.py: Every prompt as a Python constant
- run_techniques_demo.py: Bad vs good side-by-side
- run_10_prompt_demo.py: Password checker 10-level demo
- Solution prompts for all challenges"

# ==========================================
# BRANCH: solutions (from 04-challenges)
# ==========================================
echo "📦 Branch: solutions"
git checkout 04-challenges

# Overwrite challenge files with solution versions
cat > challenges/challenge_1a_bug_fixer.py << 'PYEOF'
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
PYEOF

cat > challenges/challenge_1b_documenter.py << 'PYEOF'
"""🟢 Challenge 1B: The Documenter — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read challenges/test_files/hello.py and add Google-style docstrings to every function.
Each docstring: one-line summary, Args with types, Returns with type, Example with >>>.
Save to challenges/test_files/hello_documented.py. Run it to verify it still works."""
    run_agent(task)
PYEOF

cat > challenges/challenge_2a_test_writer.py << 'PYEOF'
"""🟡 Challenge 2A: The Test Writer — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read challenges/test_files/hello.py. Create challenges/test_files/test_hello.py:
- Use unittest, at least 3 tests per function (normal + edge + special)
- Test greet(""), farewell("World"), format_name edge cases
- Test repeat_message with times=0 (empty list) and times=1
- Run: python -m unittest challenges/test_files/test_hello.py -v
- If any fail, fix and re-run."""
    run_agent(task)
PYEOF

cat > challenges/challenge_2b_scaffolder.py << 'PYEOF'
"""🟡 Challenge 2B: The Project Scaffolder — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Create a calculator project in 'my_calculator/':

1. calculator.py: Calculator class, add/subtract/multiply/divide, all return float,
   divide(a,0) raises ValueError("Cannot divide by zero")
2. test_calculator.py: unittest, 2+ tests/method, test divide-by-zero, negatives, floats
3. README.md: title, description, usage examples, divide-by-zero note

Run: python -m unittest my_calculator/test_calculator.py -v"""
    run_agent(task)
PYEOF

cat > challenges/challenge_2c_refactorer.py << 'PYEOF'
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
PYEOF

cat > challenges/challenge_3a_multi_file.py << 'PYEOF'
"""🔴 Challenge 3A: Multi-File App — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Build contact book in 'contacts/':

models.py: Contact(name,phone,email), __str__, to_dict(), from_dict() classmethod
storage.py: CONTACTS_FILE, load/save/add/delete(case-insensitive)/search(partial match)
test_contacts.py: unittest, setUp/tearDown isolation, 8+ tests, roundtrip/CRUD/search

After creating: run tests, then demo add 2 contacts, list, search, delete, list again."""
    run_agent(task)
PYEOF

cat > challenges/challenge_3b_code_reviewer.py << 'PYEOF'
"""🔴 Challenge 3B: Code Reviewer — ✅ SOLUTION"""
from agent import run_agent

if __name__ == "__main__":
    task = """Read 03_simple_agent.py. Write review_notes.md (Category/Severity/Description/Fix).

Check: run_command security (High), invalid JSON from tool args (Medium), no retries (Medium),
max_tokens truncation (Low), magic strings (Low), no logging (Medium).

Create 03_simple_agent_v2.py with top 5 fixes: BLOCKED_COMMANDS, try/except JSON,
retry logic (2 retries, 1s delay), constant for model name, timestamped logging.
Test v2: create and run test_v2.py that prints 'v2 works!'"""
    run_agent(task)
PYEOF

git checkout -b solutions
git add -A
git commit -m "Solutions: completed prompts for all challenges

Share AFTER workshop. Students compare their prompts to these."

# ==========================================
# PUSH ALL BRANCHES
# ==========================================
echo ""
echo "🚀 Pushing all branches..."
git push -u origin main
git push -u origin 01-basic-chat
git push -u origin 02-context-degradation
git push -u origin 03-simple-agent
git push -u origin 04-challenges
git push -u origin 05-prompts
git push -u origin solutions

echo ""
echo "✅ Done! All branches pushed."
echo ""
echo "Branches:"
echo "  main                   → Students clone this before workshop"
echo "  01-basic-chat          → Section 3: checkout during Mental Model"
echo "  02-context-degradation → Section 4: checkout during Context demo"
echo "  03-simple-agent        → Section 6: checkout for code-along"
echo "  04-challenges          → Section 7: checkout after break"
echo "  05-prompts             → Instructor: all demo prompts + runners"
echo "  solutions              → Share after workshop"
