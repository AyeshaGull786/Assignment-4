# 05_get_name
# Problem Statement
# Fill out the get_name() function to return your name as a string! We've written a main() function for you which 
# calls your function to retrieve your name and then prints it in a greeting.

def get_name():
    """Returns your name as a string."""
    return "Ayesha"  # Replace "Your Name" with your actual name

def main():
    """Calls get_name() and prints a greeting."""
    name = get_name()  # Call function to get name
    print("Hello,", name + "!")  # Print greeting

# Run the program
main()
