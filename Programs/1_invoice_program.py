# Program to calculate invoice total with gratuity
# This program demonstrates the use of variables, comments, and arithmetic operations

# Variables to store invoice information
client_name = "John Doe"
subtotal = 100.00  # Example subtotal amount
tax_rate = 0.07  # Sales tax rate (7%)
tip_percent = 15  # Gratuity percentage

# Arithmetic operations
tip_amount = subtotal * (tip_percent / 100)
tax_amount = subtotal * tax_rate
total_invoice = subtotal + tip_amount + tax_amount

# Displaying Invoice Information
print("\n--- INVOICE SUMMARY ---")
print(f"Client: {client_name}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Gratuity: ${tip_amount:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total Due: ${total_invoice:.2f}")