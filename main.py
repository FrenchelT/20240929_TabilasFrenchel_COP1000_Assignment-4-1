"""
This program calculates prices for custom house signs.
"""

# Prompt user input with clear messages.
numChars = int(input("Enter the number of characters for the sign: "))
woodType = input("Enter the type of wood (oak or pine): ").lower()
color = input("Enter the color of the characters (gold, black, or white): ").lower()

# Initialize the base charge for the sign.
charge = 35.00

# Add cost for additional characters beyond the first five.
if numChars > 5:
    charge += (numChars - 5) * 4

# Add cost for gold-leaf lettering.
if color == "gold":
    charge += 15.00

# Add cost for oak wood.
if woodType == "oak":
    charge += 20.00

# Ensure the charge is not less than the base charge (redundant given initialization).
if charge < 35.00:
    charge = 35.00

# Output the total charge for the sign.
print(f"The charge for this sign is ${charge:.2f}")