# Delete Multiple Files Example

from pathlib import Path

# Get files in the current directory
current_dir = Path(".")

files_to_delete = [".txt", ".zip"]

for item in current_dir.iterdir():
    # Check the extension of the file
    if item.is_file() and item.suffix in files_to_delete:
        item.unlink()  # Delete the file


# item things
# item.is_file() - checks if the item is a file
# item.suffix - gets the file extension
# item.name - gets the file name
# item.unlink() - deletes the file