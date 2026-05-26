# Unzip all zip files into individual txt files

from zipfile import ZipFile
from pathlib import Path


# Setup
current_dir = Path(".")

# Unzip files
for item in current_dir.iterdir():
    if item.is_file() and item.suffix == ".zip":
        with ZipFile(item.name, "r") as zip_file:
            zip_file.extractall()  # Extract all contents of the zip file
        item.unlink()  # Delete the original zip file after extracting