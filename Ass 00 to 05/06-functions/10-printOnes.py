# 10_print_ones_digit.
# Problem Statement
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit.
# The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

def print_ones_digit(num: int):
    """Prints the ones digit of the given number."""
    ones_digit = num % 10  # Get the last digit using modulo operator
    print(f"The ones digit of {num} is {ones_digit}")

def main():
    """Gets user input and calls print_ones_digit."""
    num = int(input("Enter an integer: "))  # Get number from user
    print_ones_digit(num)  # Call the function to print ones digit

# Run the program
if __name__ == "__main__":
    main()
