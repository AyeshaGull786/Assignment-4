# 05_subtract_7
# Problem Statement
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven 
# helper function! If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):
    """Subtracts 7 from the given number and returns the result."""
    return num - 7

def main():
    """Gets user input, calls subtract_seven, and prints the result."""
    
    # Get user input as an integer
    num = int(input("Enter a number: "))
    
    # Call the function and store the result
    result = subtract_seven(num)
    
    # Print the result
    print(f"{num} minus 7 is {result}")

# Run the program
if __name__ == "__main__":
    main()
