"""
🧞 Vibe Coding Workshop — Exercise 3: Build a Coding Agent
Section 6: The Agent Loop (Code-Along)

KEY INSIGHT: An agent is just:
  1. An LLM in a loop
  2. With tools it can call
  3. That keeps running until the task is done

That's it. Cursor, Claude Code, GitHub Copilot — they all work this way.

Run: python 03_simple_agent.py
"""

import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ==========================================
# STEP 1: DEFINE YOUR TOOLS
# ==========================================
# These are just normal Python functions.
# The agent will call them when it needs to interact with the world.

def list_files(directory="."):
    """List files in a directory."""
    try:
        files = os.listdir(directory)
        return json.dumps({"files": files})
    except Exception as e:
        return json.dumps({"error": str(e)})


def read_file(filepath):
    """Read contents of a file."""
    try:
        with open(filepath, "r") as f:
            content = f.read()
        return json.dumps({"content": content})
    except Exception as e:
        return json.dumps({"error": str(e)})


def write_file(filepath, content):
    """Write content to a file."""
    try:
        # Create parent directories if they don't exist
        parent = os.path.dirname(filepath)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)
        return json.dumps({"success": True, "message": f"Wrote to {filepath}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


def run_command(command):
    """Run a shell command and return stdout/stderr."""
    import subprocess
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True,
            text=True, timeout=10
        )
        return json.dumps({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except subprocess.TimeoutExpired:
        return json.dumps({"error": "Command timed out (10s limit)"})
    except Exception as e:
        return json.dumps({"error": str(e)})


# Map tool names → functions (so we can look them up dynamically)
TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
    "run_command": run_command,
}


# ==========================================
# STEP 2: TELL THE LLM ABOUT YOUR TOOLS
# ==========================================
# This is the "menu" — the LLM reads this to know what it CAN do.
# It's just JSON that describes each function's name, purpose, and parameters.

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List all files in a directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "The directory path to list. Defaults to current directory."
                    }
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path to the file to read"
                    }
                },
                "required": ["filepath"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to a file (creates or overwrites)",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {
                        "type": "string",
                        "description": "Path to the file to write"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write to the file"
                    }
                },
                "required": ["filepath", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Run a shell command and return stdout, stderr, and return code",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The shell command to execute"
                    }
                },
                "required": ["command"]
            }
        }
    }
]


# ==========================================
# STEP 3: THE AGENT LOOP
# ==========================================
# This is the ENTIRE magic. A while loop.

def run_agent(user_task):
    """Run the agent until it completes the task (or hits the safety limit)."""

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful coding assistant with access to the file system.\n"
                "You can list files, read files, write files, and run shell commands.\n"
                "When given a task, use your tools to accomplish it.\n"
                "Work step by step and verify your work by running the code you write."
            )
        },
        {
            "role": "user",
            "content": user_task
        }
    ]

    print(f"\n{'=' * 60}")
    print(f"🤖 TASK: {user_task[:100]}")
    print(f"{'=' * 60}\n")

    max_iterations = 10  # Safety limit — don't let it loop forever
    iteration = 0

    while iteration < max_iterations:
        iteration += 1
        print(f"--- Iteration {iteration} ---")

        # Send messages + tool definitions to the LLM
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=TOOL_DEFINITIONS,
            tool_choice="auto",  # LLM decides whether to use a tool
            max_tokens=1000
        )

        assistant_message = response.choices[0].message

        # Does the LLM want to call a tool?
        if assistant_message.tool_calls:
            # Add the assistant's message (with tool call info) to history
            # Note: content can be None when tool calls are present
            messages.append({
                "role": "assistant",
                "content": assistant_message.content or "",
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    }
                    for tc in assistant_message.tool_calls
                ]
            })

            # Execute each tool call
            for tool_call in assistant_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                # Handle None/null arguments (convert to empty dict)
                if tool_args is None:
                    tool_args = {}

                print(f"  🔧 Tool: {tool_name}")
                print(f"     Args: {json.dumps(tool_args)[:100]}")

                # Actually run the tool
                if tool_name in TOOLS:
                    result = TOOLS[tool_name](**tool_args)
                else:
                    result = json.dumps({"error": f"Unknown tool: {tool_name}"})

                print(f"     Result: {result[:150]}{'...' if len(result) > 150 else ''}")

                # Add tool result to conversation history
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

        else:
            # No tool calls — the agent is done
            final_response = assistant_message.content
            print(f"\n{'=' * 60}")
            print("✅ AGENT COMPLETE")
            print(f"{'=' * 60}")
            print(f"\n{final_response}")
            return final_response

    print("\n⚠️ Max iterations reached — agent stopped.")
    return "Max iterations reached"


# ==========================================
# STEP 4: TEST IT!
# ==========================================
if __name__ == "__main__":
    # Create a working directory for the agent
    os.makedirs("test_files", exist_ok=True)

    # ----- TEST 1: Explore files -----
    print("\n" + "=" * 60)
    print("TEST 1: List and explore files")
    print("=" * 60)
    run_agent("List all files in the current directory and tell me what you see.")

    # ----- TEST 2: Create a file -----
    print("\n" + "=" * 60)
    print("TEST 2: Create a file and run it")
    print("=" * 60)
    run_agent("""
    Create a Python file called test_files/hello.py that:
    1. Defines a function greet(name) that returns "Hello, {name}!"
    2. Has a main block that calls greet("World") and prints the result
    Then run it to verify it works.
    """)

    # ----- TEST 3: Read, modify, verify -----
    print("\n" + "=" * 60)
    print("TEST 3: Read and modify a file")
    print("=" * 60)
    run_agent(
        "Read test_files/hello.py and add a farewell(name) function "
        "that returns 'Goodbye, {name}!'. Update the main block to "
        "call both functions. Then run it to test."
    )
