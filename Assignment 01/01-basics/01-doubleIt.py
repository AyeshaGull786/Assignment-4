# 01_double_it
# Problem Statement
# Write a program that asks a user to enter a number.
# Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def double_until_100():
    """Asks the user for a number and keeps doubling it until it's 100 or more."""
    num = float(input("Enter a number: "))  # Get initial number from the user
    
    while num < 100:  # Continue doubling until 100 or more
        num *= 2  # Double the number
        print(num)  # Print the updated number

# Run the function
if __name__ == "__main__":
    double_until_100()
