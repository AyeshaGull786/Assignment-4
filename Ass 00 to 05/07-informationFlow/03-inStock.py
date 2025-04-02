# 03_in_stock.
# Problem Statement
# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and
# returns how many of that fruit are in her inventory. Write code in main() which will:
# Prompt the user to enter a fruit ("Enter a fruit: ")
# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock
# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)
# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Sample inventory (Can be replaced with real function)
inventory = {
    "apple": 50,
    "banana": 30,
    "pear": 1000,
    "orange": 75,
}

def num_in_stock(fruit: str) -> int:
    """Returns the number of a given fruit in stock."""
    return inventory.get(fruit.lower(), 0)  # Default to 0 if fruit is not found

def main():
    """Gets user input and checks stock availability."""
    fruit = input("Enter a fruit: ").strip().lower()  # Get fruit input (case-insensitive)
    
    count = num_in_stock(fruit)  # Get the stock count
    
    if count > 0:
        print("\nThis fruit is in stock! Here is how many:\n")
        print(count)
    else:
        print("\nThis fruit is not in stock.")

# Run the program
if __name__ == "__main__":
    main()
