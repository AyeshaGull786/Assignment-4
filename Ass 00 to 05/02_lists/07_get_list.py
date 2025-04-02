# 07_get_list.
# Write a program which continuously asks the user to enter values which are added one by one
# into a list. When the user presses enter without typing anything, print the list.

def get_user_input():
    """Continuously asks the user for input and stores values in a list.
       Stops when the user presses Enter without typing anything.
    """
    values = []  # Initialize an empty list

    while True:
        user_input = input("Enter a value (or press Enter to finish): ")  # Get input
        if user_input == "":  # Stop when input is empty
            break
        values.append(user_input)  # Add input to the list

    print("\nFinal List:", values)  # Print the list

# Run the function
get_user_input()
