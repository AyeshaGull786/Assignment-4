# 05_remainder_division.

# Problem Statement
# Ask the user for two numbers, one at a time, and then print the
# result of dividing the first number by the second and also the remainder of the division.

def main():
    
    #ask the user to enter two integers
    num1 = int(input("Please Enter an integer which you want to divide: "))
    num2 = int(input("Please Enter an integer which you want to divide by: "))
    
    
    # Check for division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
        return   # Exit the function early to avoid errors
        
    else:
        # Perform integer division and find remainder
        quotient: int  = num1 // num2  # Integer division
        remainder: int = num1 % num2  # Modulus (remainder)
    
     # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Call the main function
if __name__ == "__main__":
    main()

    
    