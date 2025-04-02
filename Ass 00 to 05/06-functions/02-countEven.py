# 02_count_even.

# Problem Statement
# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the 
# prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def count_even():
    """
    Prompts the user to enter integers until they press enter.
    Then, counts and prints the number of even numbers in the list.
    """
    numbers = []  # List to store user input

    # Prompt user for numbers until they press enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop when input is empty
            break
        numbers.append(int(user_input))  # Convert to integer and add to list

    # Count even numbers in the list
    even_count = sum(1 for num in numbers if num % 2 == 0)

    # Print the count of even numbers
    print("Number of even numbers:", even_count)

# Run the function
count_even()
