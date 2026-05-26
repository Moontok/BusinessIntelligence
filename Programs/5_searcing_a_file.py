# File Searching Automation Example
# This script demonstrates how to search for a specific term in a text file and report the line number and content where the term is found.


# Define the search term and the file to search
search_term = "Diana Prince"
file_name = "customer_data.txt"

line_number = 0

print("Searching file for term:", search_term)
print()

# Open the file and read it line by line
with open(file_name, "r") as file:    
    for line in file:
        line_number += 1

        # Check if the search term is in the current line
        if search_term in line:
            print(f"Found '{search_term}' on line {line_number}:")
            print("  Line Text:",line.strip())

print()
print("Search complete.")