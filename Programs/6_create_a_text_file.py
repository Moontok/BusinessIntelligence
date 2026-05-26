# File Creation Example

filename: str = "invoice.txt"

# Open the file in write mode
with open(filename, "w") as file:
    file.write("---- Invoice File ---\n")
    file.write("Customer: John Doe\n")
    file.write("Amount: $100.00\n")
    file.write("Due Date: 2024-07-01\n")
    file.write("Thank you for your business!\n")
