# Stock Price Alert
# This program monitors stock prices and triggers an alert when the price drops below a specified target.
# It demonstrates the use of lists and iteration.

# A simple list data structure to hold stock prices
price_history = [150.25, 148.50, 142.10, 139.90, 145.00]
target_price = 140.00

print("Scanning market data...")
# Iteration control structure
for price in price_history:
    if price <= target_price:
        print(f"ALERT: Price dropped to ${price}! Triggering automated buy order.")
    else:
        print(f"Current price: ${price} - no action needed.")