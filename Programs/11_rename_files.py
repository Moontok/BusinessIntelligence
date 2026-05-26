# Rename add old prefix to invoice files.

from pathlib import Path


# Setup
current_dir = Path(".")

# Rename files
for item in current_dir.iterdir():
    if item.is_file() and "invoice_" in item.name:
        new_name = f"old_{item.name}"
        item.rename(new_name)  # Rename the file with the new name