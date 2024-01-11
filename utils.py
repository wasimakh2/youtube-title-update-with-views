def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        utils.handle_error(f"File not found: {file_path}")

def write_file(file_path: str, content: str) -> None:
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except PermissionError:
        utils.handle_error(f"Permission denied: {file_path}")

def handle_error(error_message: str) -> None:
    print(f"Error: {error_message}")
