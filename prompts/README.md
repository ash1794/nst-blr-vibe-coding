# 📝 Workshop Prompts

This folder contains all prompts used during the workshop, plus scripts to run them live.

## Files

| File | Purpose |
|------|---------|
| `all_prompts.py` | All prompts as Python constants — the source of truth |
| `run_techniques_demo.py` | Runs bad vs good prompt comparisons (Section 2) |
| `run_10_prompt_demo.py` | Runs the 10-level password checker demo (Section 2) |

## Usage During Workshop

### 5 Techniques Demo (bad vs good, side-by-side)
```bash
python prompts/run_techniques_demo.py         # All 5 techniques
python prompts/run_techniques_demo.py 1 2     # Just techniques 1 and 2
```

### 10-Prompt Challenge (recommended: run levels 1, 4, 7, 10 live)
```bash
python prompts/run_10_prompt_demo.py 1 4 7 10 # The 4 key levels
python prompts/run_10_prompt_demo.py           # All 10 (takes longer)
```

## Solution Prompts

`all_prompts.py` also contains `SOLUTION_*` constants with good prompts for each challenge.
Share these **after** the workshop, or use them as instructor reference during the challenge section.
