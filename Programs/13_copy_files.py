# Copy files from old_invoices to backup_invoices
from pathlib import Path
from shutil import copy

# Setup
current_dir = Path(".")
old_dir = current_dir / "old_invoices"
backup_dir = current_dir / "backup_invoices"

# Create backup directory if it doesn't exist
if not backup_dir.exists():
    backup_dir.mkdir()

# Copy files
for item in old_dir.iterdir():
    if item.is_file():
        name = f"copy_{item.name}"
        copy(item, backup_dir / name)  # Copy the file to the backup directory
