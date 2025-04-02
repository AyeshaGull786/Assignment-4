# 05_double_it.

# Problem Statement
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result.
# It will repeat that process until the value is 100 or greater.
# Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value.
# Recall that you can double the value of curr_value using a line like:

# curr_value = curr_value * 2
# This program should have a while loop and the while loop condition should test if curr_value is less than 100. 
# Thus, your program will have the line:
# while curr_value < 100:

def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Continue doubling until the value reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=" ")   # Print the value in the same line

# Run the program
main()
