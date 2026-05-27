# ==========================================
# MODULE 1: The Product Catalog
# A dictionary storing ID, Name, Price, and Stock
# ==========================================
catalog = {
    "101": {"name": "Wireless Mouse", "price": 25.00, "stock": 10},
    "102": {"name": "Mechanical Keyboard", "price": 65.00, "stock": 4},
    "103": {"name": "USB-C Hub", "price": 40.00, "stock": 2},
    "104": {"name": "Monitor Stand", "price": 30.00, "stock": 15}
}

# ==========================================
# MODULE 2: The Shopping Cart
# A list to track the items for the current customer
# ==========================================
cart = []

print("--- Welcome to the SBE POS System ---")
print("Available Items:")
for item_id, details in catalog.items():
    print(f"[{item_id}] {details['name']} - ${details['price']} (In Stock: {details['stock']})")
print("-------------------------------------")

# The Infinite Loop (Code Blueprint Lab)
while True:
    # Prompt the cashier
    user_input = input("\nEnter Item ID to add to cart (or type 'checkout' to finish): ")
    
    if user_input.lower() == "checkout":
        break # Exit the loop and go to payment
        
    # Check if the item exists in our catalog
    if user_input in catalog:
        # Get the quantity
        qty = int(input(f"How many {catalog[user_input]['name']}s? "))
        
        # Check if we have enough in stock
        if qty <= catalog[user_input]['stock']:
            # Add it to the cart
            cart.append({"id": user_input, "quantity": qty})
            print(f"Added {qty}x {catalog[user_input]['name']} to cart.")
        else:
            print("Error: Not enough stock available!")
    else:
        print("Error: Invalid Item ID. Please try again.")

# ==========================================
# MODULE 3: The Checkout Engine
# Aggregates prices, applies rules, and prints receipt
# ==========================================
print("\n" + "="*30)
print("          RECEIPT")
print("="*30)

subtotal = 0.0

# Process each item in the cart
for item in cart:
    item_id = item["id"]
    qty = item["quantity"]
    
    product = catalog[item_id]
    line_total = product["price"] * qty
    subtotal += line_total
    
    # Print line item
    print(f"{product['name']} (x{qty}) .... ${line_total:.2f}")
    
    # INVENTORY TRACKING LINKAGE (Advanced Student Challenge)
    product["stock"] -= qty 
    if product["stock"] < 3:
        print(f"   *** LOW STOCK ALERT: Only {product['stock']} left in inventory! ***")

print("-" * 30)

# THE "FEATURE REQUEST" EXTENSION (10% discount over $100)
discount = 0.0
if subtotal > 100.00:
    discount = subtotal * 0.10
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"10% Big Spender Discount: -${discount:.2f}")

# Calculate Tax and Final Total
taxable_amount = subtotal - discount
tax_rate = 0.08 # 8% Sales tax
tax = taxable_amount * tax_rate
final_total = taxable_amount + tax

print(f"Tax (8%): ${tax:.2f}")
print("=" * 30)
print(f"TOTAL DUE: ${final_total:.2f}")
print("=" * 30)
print("Thank you for your business!\n")