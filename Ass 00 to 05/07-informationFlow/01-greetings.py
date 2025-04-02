# 01_greetings.
# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting.
# Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

def greet(name: str):
    """Prints a greeting message with the given name."""
    print(f"Hello, {name}! Welcome!")

def main():
    """Gets user's name and calls the greet function."""
    name = input("Enter your name: ")  # Take user input
    greet(name)  # Call the greet function with the user's name

# Run the program
if __name__ == "__main__":
    main()
