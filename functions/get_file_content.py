import os
from functions.config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read and return the contents from, relative to working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    working_directory_abs = os.path.abspath(working_directory)
    relative_directory_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not relative_directory_abs.startswith(working_directory_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(relative_directory_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(relative_directory_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            next_char = f.read(1)
            if len(next_char) > 0:
                file_content_string = file_content_string + f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"
        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"