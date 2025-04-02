# 05_get_first_element

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list.
# The list is guaranteed to be non-empty. 



def get_first_element(lst):
    #Prints the first element of the given non-empty list.

    print("The first element in the list is:", lst[0])
# Prompt user to enter elements one by one
user_list = []

n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

# Call the function with user input list
get_first_element(user_list)




