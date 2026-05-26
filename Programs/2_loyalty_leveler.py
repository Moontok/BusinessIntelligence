# Loyalty Leveler
# This program assigns customers to loyalty tiers based on their annual spending.
# It demonstrates the use of variables, data types, user input, and selection control structures.

# Variables
customer_input = input("Customer Name: ")
annual_spend_input = input("Enter annual spend ($): ")

# Convert from String to Float
annual_spend = float(annual_spend_input)

# Selection control structures
if annual_spend >= 1000:
    tier = "Gold (20% off next purchase)"
elif annual_spend >= 500:
    tier = "Silver (10% off next purchase)"
else:
    tier = "Bronze (5% off next purchase)"

print() # Blank line for better readability
print(f"Customer {customer_input} has been assigned to the {tier} tier.")