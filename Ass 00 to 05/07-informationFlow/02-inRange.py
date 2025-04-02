# 02_in_range.
# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n: int, low: int, high: int) -> bool:
    """Returns True if n is between low and high (inclusive), else False."""
    return low <= n <= high  # Check if n is in the range

def main():
    """Gets input and tests the in_range function."""
    n = int(input("Enter a number: "))      # Take number input
    low = int(input("Enter the lower bound: "))  # Take lower bound input
    high = int(input("Enter the upper bound: "))  # Take upper bound input
    
    result = in_range(n, low, high)  # Call the function
    print("Is in range:", result)    # Print the result

# Run the program
if __name__ == "__main__":
    main()
