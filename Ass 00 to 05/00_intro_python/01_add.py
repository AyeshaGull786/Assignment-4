# 01:  _add_two_numbers.

# Problem Statement
# Write a Python program that takes two integer inputs from the user and calculates their sum. 
# The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem,
# where the main() function guides the user through the process of entering two numbers and displays their sum.

print("This function takes 2 user input and add them")
# Function to take input, calculate sum, and display result
def main():
    # Prompt the user to enter the first number
    num1 = int(input("Enter the first number: "))  # Taking input and converting it to integer

    # Prompt the user to enter the second number
    num2 = int(input("Enter the second number: "))  # Taking input and converting it to integer

    # Calculate the sum of both numbers
    total = num1 + num2  # Adding the two integers

    # Print the result with a message
    print(f"The sum of {num1} and {num2} is: {total}")  # Displaying output

# Call the main function when the script is executed
if __name__ == '__main__':  
    main()
