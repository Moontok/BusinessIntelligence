# Move txt files to new directory
from pathlib import Path


# Setup
current_dir = Path(".")
new_dir = Path("old_invoices")

# Create new directory if it doesn't exist
if not new_dir.exists():
    new_dir.mkdir()

# Move txt files
for item in current_dir.iterdir():
    if item.is_file() and item.suffix == ".txt":
        item.rename(new_dir / item.name)  # Move the file to the new directory