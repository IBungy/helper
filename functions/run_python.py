import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python program, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run the python program from, relative to working directory.",
            ),
            "args": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(type=types.Type.STRING),
            description="Optional arguments to pass to the Python program.",
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    working_directory_abs = os.path.abspath(working_directory)
    relative_directory_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not relative_directory_abs.startswith(working_directory_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(relative_directory_abs):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python", file_path] + args, timeout=30, capture_output=True, cwd=working_directory, text=True)
        output = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            return "No output produced."
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"