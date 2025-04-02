# 04_double.
# Problem Statement
# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you 
# which asks the user for a number, calls your code for double(num) , and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4

def double(num):
    """Returns the result of multiplying num by 2."""
    return num * 2  # Multiply input by 2

def main():
    """Gets user input, calls double(), and prints the result."""
    user_input = int(input("Enter a number: "))  # Get user input as an integer
    result = double(user_input)  # Call the function
    print("Double that is", result)  # Print the result

# Run the program
main()
