
def create_file():
    """Create a file and add content to it"""
    
    filename: str = "my_file.txt"

    # Open the file in write mode
    with open(filename, "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("It is created using Python.\n")


def create_files():
    """Create 10 files and add content to them"""

    number_of_files: int = 10

    for i in range(number_of_files):
        filename: str = f"file_{i}.txt"
        with open(filename, "w") as file:
            file.write(f"This is file number {i}.\n")
            file.write(f"It is created using Python.\n")
            file.write(f"Filename: {filename}\n")


def delete_files():
    """Delete all txt files in the current directory"""

    import os

    # Get the current directory
    current_directory: str = os.getcwd()

    # Get all files in the current directory
    files: list = os.listdir(current_directory)

    # Loop through all files
    for file in files:
        # Check if the file is a txt file
        if file.endswith(".txt"):
            # Delete the file
            os.remove(file)


def zip_files():
    """Zip each file in the current directory that ends with .txt"""

    import os
    import zipfile

    # Get the current directory
    current_directory: str = os.getcwd()

    # Get all files in the current directory
    files: list = os.listdir(current_directory)

    # Loop through all files
    for file in files:
        # Check if the file is a txt file
        if file.endswith(".txt"):
            # Create a zip file
            with zipfile.ZipFile(f"{file}.zip", "w") as zip_file:
                # Add the file to the zip file
                zip_file.write(file)
                os.remove(file)


def unzip_files():
    """Unzip each file in the current directory that ends with .zip"""

    import os
    import zipfile

    # Get the current directory
    current_directory: str = os.getcwd()

    # Get all files in the current directory
    files: list = os.listdir(current_directory)

    # Loop through all files
    for file in files:
        # Check if the file is a zip file
        if file.endswith(".zip"):
            # Extract the zip file
            with zipfile.ZipFile(file, "r") as zip_file:
                zip_file.extractall()
            
            os.remove(file)


def move_files():
    """Move all txt files to overthere directory"""

    import os
    import shutil

    # Get the current directory
    current_directory: str = os.getcwd()

    # Get all files in the current directory
    files: list = os.listdir(current_directory)

    # Create a new directory
    new_directory: str = "overthere"
    os.mkdir(new_directory)

    # Loop through all files
    for file in files:
        # Check if the file is a txt file
        if file.endswith(".txt"):
            # Move the file to the new directory
            shutil.move(file, new_directory)