# This program calculates prices for custom house signs.

# Declare and initialize variables here.
charge = 35.00  # Base charge for the sign

# Prompt user for input
num_chars = int(input("Enter the number of characters on the sign: "))
wood_type = input("Enter the type of wood (e.g., oak, pine): ")
color = input("Enter the color of characters (e.g., black, white, gold): ")

# Calculate additional charge based on the number of characters.
if num_chars > 5:
    charge += (num_chars - 5) * 4

# Add cost for character color.
if color.lower() == "gold":
    charge += 15

# Add cost for wood type.
if wood_type.lower() == "oak":
    charge += 20

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
