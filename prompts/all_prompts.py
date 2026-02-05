"""
🧞 Vibe Coding Workshop — Prompt Reference
All prompts used during the workshop, organized by section.

This file is a REFERENCE, not something you run.
Use it during the workshop to copy-paste prompts for live demos.
"""

# ==========================================
# SECTION 2: THE 5 TECHNIQUES
# ==========================================

# --- Technique 1: Be Painfully Specific ---

TECHNIQUE_1_BAD = "Write a function to sort a list"

TECHNIQUE_1_GOOD = """Write a Python function called sort_scores that:
- Takes a list of integers as input
- Returns a new list sorted in descending order
- Does not modify the original list
- Returns an empty list if input is empty"""

# --- Technique 2: One-Shot Prompting ---

TECHNIQUE_2_BAD = "Format these names nicely"

TECHNIQUE_2_GOOD = """Format these names like this example:

Input:  'john doe'
Output: 'Doe, John'

Now format these:
- 'jane smith'
- 'ravi kumar'
- 'anna maria gonzalez'"""

# --- Technique 3: Define Output Format ---

TECHNIQUE_3_BAD = "Tell me about Python data types"

TECHNIQUE_3_GOOD = """List Python's 5 most common data types. For each one:
- Name
- One-line description
- One code example (single line)

Format as a numbered list."""

# --- Technique 4: Set Constraints ---

TECHNIQUE_4_BAD = "Write a function to find duplicates in a list"

TECHNIQUE_4_GOOD = """Write a Python function find_duplicates(items: list) -> list

CONSTRAINTS:
- Must run in O(n) time complexity
- Use only built-in Python (no imports)
- Return duplicates in the order they first appear
- Return empty list if no duplicates"""

# --- Technique 5: Chain of Thought ---

TECHNIQUE_5_BAD = "Build me a student management system"

TECHNIQUE_5_GOOD = """Let's build a student management system step by step.

Step 1: First, just write the Student class with these
        attributes: name (str), roll_no (int), grades (dict)
        Include a method to calculate GPA.

(I'll ask for the next step after we get this right.)"""


# ==========================================
# SECTION 2: THE 10-PROMPT CHALLENGE
# Password Strength Checker — from garbage to perfect
# ==========================================

LEVEL_01 = "check password"

LEVEL_02 = "Write code to check if a password is strong"

LEVEL_03 = "Write a Python function to check if a password is strong enough"

LEVEL_04 = """Write a Python function to check password strength.
It should check for: length, uppercase letters, lowercase letters,
numbers, and special characters."""

LEVEL_05 = """Write a Python function check_password_strength(password: str) -> bool

A password is strong if ALL of these are true:
- At least 8 characters long
- Contains at least 1 uppercase letter
- Contains at least 1 lowercase letter
- Contains at least 1 digit
- Contains at least 1 special character from: !@#$%^&*"""

LEVEL_06 = """Write a Python function check_password_strength(password: str) -> dict

Return a dictionary with:
- "is_strong": bool (True if ALL checks pass)
- "checks": dict with each check name mapped to True/False

Checks:
- "length": at least 8 characters
- "uppercase": at least 1 uppercase letter (A-Z)
- "lowercase": at least 1 lowercase letter (a-z)
- "digit": at least 1 digit (0-9)
- "special": at least 1 character from !@#$%^&*()_+-="""

LEVEL_07 = """Write a Python function check_password_strength(password: str) -> dict

Return a dictionary with:
- "is_strong": bool (True if ALL checks pass)
- "checks": dict with each check name mapped to True/False

Checks:
- "length": at least 8 characters
- "uppercase": at least 1 uppercase letter (A-Z)
- "lowercase": at least 1 lowercase letter (a-z)
- "digit": at least 1 digit (0-9)
- "special": at least 1 character from !@#$%^&*()_+-=

EDGE CASES:
- Empty string → all checks fail
- None input → raise TypeError with message "Password must be a string"
- Whitespace-only → length check should count whitespace
  but the password should still need other character types"""

LEVEL_08 = """Write a Python function check_password_strength(password: str) -> dict

Return a dictionary with:
- "is_strong": bool (True if ALL checks pass)
- "checks": dict with each check name mapped to True/False

Checks:
- "length": at least 8 characters
- "uppercase": at least 1 uppercase letter (A-Z)
- "lowercase": at least 1 lowercase letter (a-z)
- "digit": at least 1 digit (0-9)
- "special": at least 1 character from !@#$%^&*()_+-=

EDGE CASES:
- Empty string → all checks fail
- None input → raise TypeError with message "Password must be a string"
- Whitespace-only → length check should count whitespace
  but the password should still need other character types

EXAMPLE:
Input:  check_password_strength("Hello1!")
Output: {
    "is_strong": False,
    "checks": {
        "length": False,
        "uppercase": True,
        "lowercase": True,
        "digit": True,
        "special": True
    }
}"""

LEVEL_09 = """Write a Python function check_password_strength(password: str) -> dict

Return a dictionary with:
- "is_strong": bool (True if ALL checks pass)
- "checks": dict with each check name mapped to True/False

Checks:
- "length": at least 8 characters
- "uppercase": at least 1 uppercase letter (A-Z)
- "lowercase": at least 1 lowercase letter (a-z)
- "digit": at least 1 digit (0-9)
- "special": at least 1 character from !@#$%^&*()_+-=

EDGE CASES:
- Empty string → all checks fail
- None input → raise TypeError with message "Password must be a string"
- Whitespace-only → length check should count whitespace
  but the password should still need other character types

EXAMPLE:
Input:  check_password_strength("Hello1!")
Output: {
    "is_strong": False,
    "checks": {
        "length": False,
        "uppercase": True,
        "lowercase": True,
        "digit": True,
        "special": True
    }
}

MUST PASS THESE TESTS:
- check_password_strength("Abcdef1!")["is_strong"] == True
- check_password_strength("abcdef1!")["is_strong"] == False  # no uppercase
- check_password_strength("ABCDEF1!")["is_strong"] == False  # no lowercase
- check_password_strength("Abcdefg!")["is_strong"] == False  # no digit
- check_password_strength("Abcdefg1")["is_strong"] == False  # no special
- check_password_strength("Ab1!")["is_strong"] == False      # too short
- check_password_strength("")["is_strong"] == False
- check_password_strength(None) raises TypeError"""

LEVEL_10 = """Write a Python function with these exact specifications:

FUNCTION: check_password_strength(password: str) -> dict
MODULE: No external imports. Use only Python builtins and `re` (regex).

BEHAVIOR:
Return a dict with keys "is_strong" (bool) and "checks" (dict).
"is_strong" is True ONLY if all individual checks pass.
"checks" maps each rule name to its pass/fail status (bool).

RULES:
| Check Name   | Rule                              |
|------------- |-----------------------------------|
| "length"     | len(password) >= 8                |
| "uppercase"  | at least 1 char in A-Z            |
| "lowercase"  | at least 1 char in a-z            |
| "digit"      | at least 1 char in 0-9            |
| "special"    | at least 1 char in !@#$%^&*()_+-= |

EDGE CASES:
- Empty string "" → all checks return False
- None → raise TypeError("Password must be a string")
- Whitespace counts toward length but not other categories
- Unicode letters (é, ñ) do NOT count as uppercase/lowercase

EXAMPLE:
Input:  check_password_strength("Hello1!")
Output: {"is_strong": False, "checks": {"length": False, "uppercase": True,
         "lowercase": True, "digit": True, "special": True}}

TESTS THAT MUST PASS:
- check_password_strength("Abcdef1!")["is_strong"] == True
- check_password_strength("abcdef1!")["is_strong"] == False
- check_password_strength("ABCDEF1!")["is_strong"] == False
- check_password_strength("Abcdefg!")["is_strong"] == False
- check_password_strength("Abcdefg1")["is_strong"] == False
- check_password_strength("Ab1!")["is_strong"] == False
- check_password_strength("")["is_strong"] == False
- check_password_strength(None) → TypeError
- check_password_strength("Café123!")["checks"]["uppercase"] == True
- check_password_strength("Café123!")["checks"]["lowercase"] == True
  (the 'é' should NOT satisfy lowercase — only a-z)

STYLE:
- Include docstring
- Include inline comments for non-obvious logic
- No classes, just a standalone function"""


# ==========================================
# SECTION 5: RPI FRAMEWORK EXAMPLES
# ==========================================

RPI_BAD_FIZZBUZZ = "Write FizzBuzz in Python"

RPI_GOOD_FIZZBUZZ = """Write a Python function with these specifications:

FUNCTION: fizzbuzz(n: int) -> str

BEHAVIOR:
- If n is divisible by 3 only: return "Fizz"
- If n is divisible by 5 only: return "Buzz"
- If n is divisible by both 3 and 5: return "FizzBuzz"
- Otherwise: return str(n)

TEST CASES TO PASS:
- fizzbuzz(3) == "Fizz"
- fizzbuzz(5) == "Buzz"
- fizzbuzz(15) == "FizzBuzz"
- fizzbuzz(7) == "7"
- fizzbuzz(1) == "1"

CONSTRAINTS:
- No external libraries
- Must handle negative numbers (same rules apply)
- Must handle zero (divisible by everything, so "FizzBuzz")"""


# ==========================================
# SECTION 7: CHALLENGE SOLUTION PROMPTS
# These are "good" prompts for each challenge.
# Share AFTER the workshop or use as instructor reference.
# ==========================================

SOLUTION_1A_BUG_FIXER = """Read the file challenges/test_files/buggy.py and do the following:

1. First, run it with: python challenges/test_files/buggy.py
2. Observe all errors and incorrect outputs
3. Fix ALL bugs. The known issues are:
   - calculate_average crashes on empty list
   - find_max returns wrong result for all-negative lists
   - reverse_string has an index error
   - count_words miscounts with multiple spaces
4. After fixing, run it again
5. Verify these expected outputs:
   - Test 1: 20.0
   - Test 2: 0
   - Test 3: -2
   - Test 4: olleh
   - Test 5: 2"""

SOLUTION_1B_DOCUMENTER = """Read challenges/test_files/hello.py and add Google-style docstrings
to every function.

Each docstring should include:
- One-line summary
- Args section with type and description for each parameter
- Returns section with type and description
- Example section with a usage example

Save the documented version to challenges/test_files/hello_documented.py.
Then run it to verify the code still works."""

SOLUTION_2A_TEST_WRITER = """Read challenges/test_files/hello.py to understand all functions.

Create challenges/test_files/test_hello.py with unit tests:
- Use Python's unittest module
- At least 3 tests per function:
  1. Normal/expected input
  2. Edge case (empty string, zero, empty list)
  3. Type boundary (numbers as strings, etc.)

For repeat_message, also test:
- times=0 should return empty list
- times=1 should return list with one element

Run the tests with: python -m unittest challenges/test_files/test_hello.py -v
If any test fails, fix it and re-run."""

SOLUTION_2B_SCAFFOLDER = """Create a Python calculator project in the folder 'my_calculator/' with these files:

1. my_calculator/calculator.py
   - Calculator class with methods: add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
   - All methods accept int or float arguments
   - divide(a, 0) should raise ValueError with message "Cannot divide by zero"
   - All methods return float

2. my_calculator/test_calculator.py
   - Use unittest module
   - At least 2 tests per method (normal case + edge case)
   - Test divide by zero raises ValueError
   - Test with negative numbers
   - Test with floats (0.1 + 0.2 should be approximately 0.3)

3. my_calculator/README.md
   - Title: "Simple Calculator"
   - Description: one paragraph
   - Usage example showing all 4 operations
   - Note about divide-by-zero behavior

After creating everything, run: python -m unittest my_calculator/test_calculator.py -v"""

SOLUTION_2C_REFACTORER = """Read challenges/test_files/messy.py and do the following:

1. Run it first and record the EXACT output (this is our expected behavior)

2. Refactor the code with these improvements:
   - Function f → compute_absolute_difference (or whatever accurately describes it)
   - Function g → remove_duplicates
   - Function h → count_vowels
   - All single-letter parameters → descriptive names
   - PEP 8 formatting (4-space indent, spaces around operators)
   - Type hints on all functions
   - Google-style docstrings on all functions
   - Comments explaining the logic in compute_absolute_difference (the branching is non-obvious)

3. Save to challenges/test_files/messy_clean.py

4. Run the clean version and verify the output EXACTLY matches the original:
   - f(3,4) and compute_absolute_difference(3,4) must give same result
   - Same for all test inputs: (3,4), (-3,4), (3,-4), (-3,-4)
   - g([1,2,2,3,3,3]) and remove_duplicates([1,2,2,3,3,3]) must match
   - h("hello world") and count_vowels("hello world") must match"""

SOLUTION_3A_MULTI_FILE = """Build a contact book application in the folder 'contacts/':

contacts/models.py:
- Contact class with attributes: name (str), phone (str), email (str)
- __init__ takes all three as required arguments
- __str__ returns "Name: {name} | Phone: {phone} | Email: {email}"
- to_dict() returns a dictionary representation
- from_dict(data) class method that creates a Contact from a dictionary

contacts/storage.py:
- CONTACTS_FILE = "contacts/contacts.json"
- load_contacts() -> list[Contact]: loads from JSON file, returns empty list if file doesn't exist
- save_contacts(contacts: list[Contact]) -> None: saves to JSON file
- add_contact(contact: Contact) -> None: loads, appends, saves
- delete_contact(name: str) -> bool: removes by name (case-insensitive), returns True if found
- search_contacts(query: str) -> list[Contact]: searches name, phone, and email (case-insensitive)

contacts/app.py:
- CLI menu with options: 1. Add contact, 2. List all, 3. Search, 4. Delete, 5. Exit
- Uses input() for user interaction
- Prints formatted output

contacts/test_contacts.py:
- Test Contact creation and to_dict/from_dict roundtrip
- Test add, load, save, delete, search
- Use setUp/tearDown to create and clean up a test JSON file
- At least 8 test cases total

After creating all files:
1. Run tests: python -m unittest contacts/test_contacts.py -v
2. Fix any failures
3. Demonstrate by running these commands programmatically:
   - Add contact: "Arjun Kumar", "9876543210", "arjun@nst.edu"
   - Add contact: "Priya Sharma", "9123456789", "priya@nst.edu"
   - List all (should show both)
   - Search for "arjun" (should find 1)
   - Delete "Priya Sharma" (should succeed)
   - List all (should show only Arjun)"""

SOLUTION_3B_CODE_REVIEWER = """Read 03_simple_agent.py and perform a structured code review.

ANALYSIS (write to review_notes.md):
For each issue found, provide:
- Category: Bug / Security / Robustness / Style
- Severity: High / Medium / Low
- Description of the issue
- Suggested fix

Specifically look for:
1. SECURITY: run_command has no restrictions — could delete files, install malware, etc.
2. BUG: What happens if tool_call.function.arguments contains invalid JSON?
3. BUG: What if the LLM returns a tool name that doesn't exist in TOOLS?
4. ROBUSTNESS: No retry logic if API call fails (network error, rate limit)
5. ROBUSTNESS: max_tokens=1000 might truncate complex responses
6. STYLE: Magic strings (model name) should be constants
7. MISSING: No logging — hard to debug when things go wrong

After the review:
1. Create 03_simple_agent_v2.py with the top 5 fixes implemented
2. Run the v2 agent with task: "Create a file called test_v2.py that prints 'v2 works!' and run it"
3. Verify it completes successfully"""
