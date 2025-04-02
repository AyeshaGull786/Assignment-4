# 08_print_multiple
# Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number 
# of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

def print_multiple(message: str, repeats: int):
    """Prints the given message the specified number of times."""
    for _ in range(repeats):  # Loop repeats times
        print(message)  # Print the message

def main():
    """Gets user input and calls print_multiple."""
    message = input("Enter a message: ")  # Get the message from the user
    repeats = int(input("Enter number of repeats: "))  # Get the repeat count
    print_multiple(message, repeats)  # Call function to print message

# Run the program
if __name__ == "__main__":
    main()
