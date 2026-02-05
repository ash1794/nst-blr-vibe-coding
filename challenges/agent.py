"""
🧞 Shared Agent — Import this in your challenges.

This is the same agent from 03_simple_agent.py, packaged as a reusable module.
All challenges import `run_agent` from here.

You should NOT need to edit this file (but you CAN for Tier 3 challenges).
"""

import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ==========================================
# TOOLS
# ==========================================

def list_files(directory="."):
    try:
        files = os.listdir(directory)
        return json.dumps({"files": files})
    except Exception as e:
        return json.dumps({"error": str(e)})


def read_file(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
        return json.dumps({"content": content})
    except Exception as e:
        return json.dumps({"error": str(e)})


def write_file(filepath, content):
    try:
        parent = os.path.dirname(filepath)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)
        return json.dumps({"success": True, "message": f"Wrote to {filepath}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


def run_command(command):
    import subprocess
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=10
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


TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
    "run_command": run_command,
}

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
                        "description": "Directory path to list. Defaults to current directory."
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
                        "description": "Path to write"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write"
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
                        "description": "Shell command to execute"
                    }
                },
                "required": ["command"]
            }
        }
    }
]


# ==========================================
# THE AGENT LOOP
# ==========================================

def run_agent(user_task, system_prompt=None, max_iterations=10):
    """Run the agent on a task.

    Args:
        user_task: What you want the agent to do.
        system_prompt: Optional custom system prompt (for Tier 3 challenges).
        max_iterations: Safety limit for the loop.

    Returns:
        The agent's final text response.
    """
    if system_prompt is None:
        system_prompt = (
            "You are a helpful coding assistant with access to the file system.\n"
            "You can list files, read files, write files, and run shell commands.\n"
            "When given a task, use your tools to accomplish it.\n"
            "Work step by step and verify your work by running the code you write."
        )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_task}
    ]

    print(f"\n{'=' * 60}")
    print(f"🤖 TASK: {user_task[:100]}{'...' if len(user_task) > 100 else ''}")
    print(f"{'=' * 60}\n")

    iteration = 0

    while iteration < max_iterations:
        iteration += 1
        print(f"--- Iteration {iteration} ---")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=TOOL_DEFINITIONS,
            tool_choice="auto",
            max_tokens=1000
        )

        assistant_message = response.choices[0].message

        if assistant_message.tool_calls:
            messages.append({
                "role": "assistant",
                "content": assistant_message.content,
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

            for tool_call in assistant_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                print(f"  🔧 Tool: {tool_name}")
                print(f"     Args: {json.dumps(tool_args)[:100]}")

                if tool_name in TOOLS:
                    result = TOOLS[tool_name](**tool_args)
                else:
                    result = json.dumps({"error": f"Unknown tool: {tool_name}"})

                print(f"     Result: {result[:150]}{'...' if len(result) > 150 else ''}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
        else:
            final_response = assistant_message.content
            print(f"\n{'=' * 60}")
            print("✅ AGENT COMPLETE")
            print(f"{'=' * 60}")
            print(f"\n{final_response}")
            return final_response

    print("\n⚠️ Max iterations reached.")
    return "Max iterations reached"
