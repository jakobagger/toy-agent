import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not is_within_directory(full_path, working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{full_path}" is not a directory'
    else:
        files_info = ""
        try:
            with os.scandir(full_path) as items:
                for item in items:
                    size = item.stat().st_size
                    is_dir = item.is_dir()  
                    files_info += f"- {item.name}: file_size={size}, is_dir={is_dir}\n"
        except Exception as e:
            return f"Error: could not get file info due to exception: {e}"
        return files_info

def is_within_directory(abs_path: str, working_dir: str) -> bool:
    abs_path = os.path.realpath(abs_path)
    working_dir = os.path.realpath(working_dir)
    return os.path.commonpath([abs_path, working_dir]) == working_dir