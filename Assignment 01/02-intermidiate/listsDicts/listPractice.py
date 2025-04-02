# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
# Print the length of the list.
# Add 'mango' at the end of the list. 
# Print the updated list.

def main():
    # 🎯 Step 1: Create a list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(f"Fruit list: {fruit_list}")
    
    # 🎯 Step 2: Print the length of the list
    print("Length of the fruit list:", len(fruit_list))

    # 🎯 Step 3: Add 'mango' to the end of the list
    fruit_list.append('mango')

    # 🎯 Step 4: Print the updated list
    print("Updated fruit list:", fruit_list)

# Run the main function
if __name__ == "__main__":
    main()

