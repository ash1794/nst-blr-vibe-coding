# 🧞 Vibe Coding Workshop: Building Mental Models for AI-Assisted Development

**Duration:** 3 hours | **Audience:** PSP-level students (early programming)

Learn how LLMs actually work, why prompting is engineering, and build a working coding agent from scratch.

---

## 🚀 Setup (Do This BEFORE the Workshop)

### 1. Get a Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up (no credit card needed)
3. Click **"Create API Key"** → Copy and save it

> Free tier: ~14,400 requests/day — more than enough for the workshop.

### 2. Clone This Repo
```bash
git clone <repo-url>
cd vibe-coding-workshop
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Your API Key
```bash
cp .env.example .env
# Open .env and paste your Groq API key
```

### 5. Verify Setup
```bash
python 00_setup_test.py
```
You should see: `✅ Setup complete! You're ready for the workshop.`

---

## 📁 Workshop Structure

| File | Section | What You'll Learn |
|------|---------|-------------------|
| `00_setup_test.py` | Pre-workshop | Verify your API key works |
| `01_basic_chat.py` | The Mental Model | LLMs are stateless — it's just an array |
| `02_context_degradation.py` | Context Limits | Watch the AI forget things |
| `03_simple_agent.py` | Build Your Agent | The core agent loop (code-along) |

### Challenges (Second Half)

| File | Tier | Challenge |
|------|------|-----------|
| `challenges/challenge_1a_bug_fixer.py` | 🟢 Warm-up | Give the agent a buggy file to fix |
| `challenges/challenge_1b_documenter.py` | 🟢 Warm-up | Agent adds docstrings to code |
| `challenges/challenge_2a_test_writer.py` | 🟡 Build | Agent writes and runs unit tests |
| `challenges/challenge_2b_scaffolder.py` | 🟡 Build | Agent creates an entire project |
| `challenges/challenge_2c_refactorer.py` | 🟡 Build | Agent cleans up messy code |
| `challenges/challenge_3a_multi_file.py` | 🔴 Boss | Agent builds a multi-file app |
| `challenges/challenge_3b_code_reviewer.py` | 🔴 Boss | Agent reviews its own code |

### Input Files (for challenges)

| File | Used By |
|------|---------|
| `challenges/test_files/buggy.py` | Challenge 1A |
| `challenges/test_files/messy.py` | Challenge 2C |
| `challenges/test_files/hello.py` | Challenge 1B, 2A |

---

## 🧠 Key Concepts

### The Genie Analogy
LLMs are like genies — they follow your **words**, not your **intent**. The more specific your prompt, the better the output.

### The 5 Prompt Engineering Techniques
1. **Be Painfully Specific** — Don't leave room for interpretation
2. **One-Shot Prompting** — Show an example of what you want
3. **Define Output Format** — Tell it the shape of the answer
4. **Set Constraints** — Narrow the solution space
5. **Chain of Thought** — Break complex tasks into steps

### The RPI Framework
- **R**esearch — What exactly am I building?
- **P**lan — Break it into verifiable steps
- **I**mplement — Give AI specs, not wishes

### The 4 Agent Primitives
Every coding agent (Cursor, Claude Code, etc.) is just:
```
list_files  → See the codebase
read_file   → Understand files
write_file  → Make changes
run_command → Test the work
```

---

## 📚 Resources

- [Geoffrey Huntley — How to Build a Coding Agent](https://github.com/ghuntley/how-to-build-a-coding-agent)
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Chris & Jack — Outsmarting a Genie](https://www.youtube.com/watch?v=lM0teS7PFMo) (the video from Section 1)

---

*Workshop by Newton School of Technology — PSP Cohort | v2.0 — February 2026*
