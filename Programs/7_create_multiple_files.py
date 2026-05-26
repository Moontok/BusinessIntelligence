# Create Multiple Files Example

# Open the file in write mode
number_of_files = 10

file_count = 0

while file_count < number_of_files:
    filename = f"invoice_{file_count + 1}.txt"
    with open(filename, "w") as file:
        file.write(f"This is {filename}\n")
    file_count += 1