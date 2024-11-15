
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply discount if it's 20% or higher
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # If discount is lower than 20%, return the original price
        return price

# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function to calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${final_price:.2f}")
