# 03_feet_to_inches

# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Conversion factor. There are 12 inches for 1 foot.
INCHES_IN_FOOT: int = 12

def convert_feet_to_inches(feet: float) -> float:
    """
    Converts feet to inches.
    """
    inches = feet * 12
    return inches

def main():
    # Ask the user for input
    feet = float(input("\nEnter length in feet: "))

    # Convert to inches
    inches = convert_feet_to_inches(feet)

    # Print the result
    print(f"\n{feet} feet is equal to {inches} inches.")

# Call main function
if __name__ == "__main__":
    main()
