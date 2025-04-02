# 08_shorten
# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, 
# and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you
# should leave it unchanged. We've written a main() function for you which gets a list and passes it into your 
# function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to
# change it around to test your program.

MAX_LENGTH = 5  # Maximum allowed length of the list

def shorten(lst):
    """Removes elements from the end of the list until its length is MAX_LENGTH.
       Prints each removed item.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove last item
        print("Removed:", removed_item)  # Print removed item

# Example function to test
def main():
    user_list = ["apple", "banana", "cherry", "date", "elderberry", "banana", ""]  # Example list
    print("Original List:", user_list)
    shorten(user_list)
    print("Shortened List:", user_list)

# Run the main function
main()
