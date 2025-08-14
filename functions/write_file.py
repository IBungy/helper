import os
from google.genai import types

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

def write_file(working_directory, file_path, content):
    working_directory_abs = os.path.abspath(working_directory)
    relative_directory_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not relative_directory_abs.startswith(working_directory_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(os.path.dirname(relative_directory_abs)):
            os.makedirs(os.path.dirname(relative_directory_abs))
    except Exception as e:
        return f"Error: {str(e)}"
    try:
        with open(relative_directory_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"   
    
