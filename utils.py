import os

def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError::
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

import os

def write_error_log(error_message: str) -> None:
    file_path = 'error_logs.txt'
    with open(file_path, 'a') as file:
        file.write(error_message + '\n'):
    print(f"Error: {error_message}")
