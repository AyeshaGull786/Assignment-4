# 04_multiple_returns
# Problem Statement
# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable

# Asks the user for their last name and stores it in a variable

# Asks the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked

# You can return multiple pieces of data by separating each piece with a comma in the return line.

def get_user_data():
    """Asks user for first name, last name, and email, then returns them."""
    
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    email = input("Enter your email address: ").strip()
    
    return first_name, last_name, email  # Return multiple values as a tuple

def main():
    """Gets user data and prints it."""
    
    # Call the function and unpack returned values
    first, last, email = get_user_data()
    
    # Print user data
    print("\nUser Data Collected:")
    print(f"First Name: {first}")
    print(f"Last Name: {last}")
    print(f"Email: {email}")

# Run the program
if __name__ == "__main__":
    main()
