import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file in which to write the content, relative to working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write in the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

def get_files_info(working_directory, directory="."):
    working_directory_abs = os.path.abspath(working_directory)
    relative_directory_abs = os.path.abspath(os.path.join(working_directory, directory))
    if not relative_directory_abs.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(relative_directory_abs):
        return f'Error: "{directory}" is not a directory'
    try:
        results = []
        for item in os.listdir(relative_directory_abs):
            results.append(f"- {item}: file_size={os.path.getsize(os.path.join(relative_directory_abs, item))} bytes, is_dir={os.path.isdir(os.path.join(relative_directory_abs, item))}")
        return "\n".join(results)
    except Exception as e:
        return f"Error: {str(e)}"