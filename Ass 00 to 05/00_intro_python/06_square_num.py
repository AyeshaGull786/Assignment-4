# 06_square_number

# Problem Statement
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

def main():
     # Prompt the user for a number
    number = float(input("Type a number to see it's aquare: "))
    
     # Calculate the square of the number
    square = number*number
    
    # Print the result
    print(f"{number:.1f} squared is {square:.1f}")
    
# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
    
    