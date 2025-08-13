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