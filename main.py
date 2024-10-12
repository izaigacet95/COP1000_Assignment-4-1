# This program calculates prices for custom house signs.

# Declare and initialize variables here.
charge = 35.00    # Base charge for this sign.
additional_charge = 4.00    # Charge for additional characters beyond the first 5.

# Prompt user for input
num_chars = int(input("Enter the number of characters on the sign: "))   # Number of characters
wood_type = input("Enter the type of wood: ")    # Type of wood
color = input("Enter the color of characters: ")    # Color of characters

# Calculate additional charges for characters beyond 5.
if num_chars > 5:
    charge += (num_chars - 5) * additional_charge

# Add cost for Color of character.
if color.lower() == "gold":
    charge += 15

# Add cost for Type of wood.
if wood_type.lower() == "oak":
    charge += 20

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))