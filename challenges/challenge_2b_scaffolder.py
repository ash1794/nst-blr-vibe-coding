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
