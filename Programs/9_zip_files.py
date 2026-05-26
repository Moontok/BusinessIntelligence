# Zip all txt files into one zip file

from zipfile import ZipFile
from pathlib import Path


# Setup
current_dir = Path(".")

# Create a zip file
with ZipFile("txt_files.zip", "w") as zip_file:
    for item in current_dir.iterdir():
        if item.is_file() and item.suffix == ".txt":
            zip_file.write(item.name)
            item.unlink()  # Delete the original txt file after zipping
