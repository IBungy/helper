import os

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
    
