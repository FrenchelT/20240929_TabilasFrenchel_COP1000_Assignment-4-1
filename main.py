"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.

# Charge for this sign.
charge = 0.00
charge = 35.00
# Number of characters.
color = "gold"
# Color of characters.
numChars = 8
# Type of wood.
woodType = "oak"

# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge += (numChars - 5) * 4
if color == "gold":
    charge += 15.00
if woodType == "oak":
    charge += 20.00
if charge < 35.00:
    charge = 35.00
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
