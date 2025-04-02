# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:
# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get
# comfortable with indexing, slicing, and modifying list elements.

# Step 1: Initialize a List
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Step 2: Function to Access Elements
def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range!"

# Step 3: Function to Modify Elements
def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Modified list: {lst}"
    else:
        return "Index out of range!"

# Step 4: Function to Slice the List
def slice_list(lst, start, end):
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start < end:
        return f"Sliced list: {lst[start:end]}"
    else:
        return "Invalid range!"

# Step 5: User Interaction
def index_game():
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))
        
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
        
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))
        
        elif choice == '4':
            print("Exiting game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again!")

# Run the game
index_game()
