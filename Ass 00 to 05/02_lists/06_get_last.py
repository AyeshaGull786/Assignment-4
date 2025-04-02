# 06_get_last_element

# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last
# element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    """Prints the last element of a given non-empty list."""
    print("The last element in the list is:", lst[-1])  # Access last element using negative indexing

# Prompt user to enter elements one by one
user_list = []

n = int(input("Enter the number of elements in the list: "))  # Ask for number of elements

for i in range(n):
    element = input(f"Enter element {i+1}: ")  # Take input for each element
    user_list.append(element)  # Add element to list

# Call the function with user input list
get_last_element(user_list)
