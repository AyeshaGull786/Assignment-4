# Password Generator in Python
# Description:
# This program generates a **strong, random password** based on user-defined preferences.
# The user can choose the password length and whether to include:
# ✔ Uppercase Letters
# ✔ Lowercase Letters
# ✔ Numbers
# ✔ Special Characters

import random  # Import random module for generating random choices
import string  # Import string module for predefined character sets

# Function to generate a random password
def generate_password(length, use_uppercase, use_numbers, use_special):

    # Define character sets based on user choices
    lowercase_letters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = string.ascii_uppercase if use_uppercase else ""  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = string.digits if use_numbers else ""  # '0123456789'
    special_chars = string.punctuation if use_special else ""  # '!@#$%^&*()_+{}[]...'

    # Combine all selected characters
    all_characters = lowercase_letters + uppercase_letters + numbers + special_chars

    # Ensure at least one character type is selected
    if not all_characters:
        print("Error: You must select at least one character type for the password.")
        return None  # Return None if no valid character set is chosen

    # Generate password by randomly choosing characters from the selected sets
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password


# Function to get valid user input for password length
def get_password_length():
    #Prompts the user to enter a valid password length (minimum 6 characters).
   
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length >= 6:
                return length  # Return valid length
            else:
                print("Password length should be at least 6 characters.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


# Function to get yes/no user input for character type selection
def get_yes_no_input(prompt):
   
    #Prompts the user with a Yes/No question and returns True/False.
   
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Invalid input! Please enter 'y' for Yes or 'n' for No.")


# Main function to interact with the user and generate the password
def main():
    
    #Runs the interactive password generator.
   
    print("🔐 Welcome to the Password Generator 🔐\n")

    # Get user preferences
    length = get_password_length()  # Get valid password length
    use_uppercase = get_yes_no_input("Include uppercase letters?")
    use_numbers = get_yes_no_input("Include numbers?")
    use_special = get_yes_no_input("Include special characters?")

    # Generate the password based on user choices
    password = generate_password(length, use_uppercase, use_numbers, use_special)

    # Display the generated password
    if password:
        print("\n✅ Your Secure Password: " + password)


# Run the program
if __name__ == "__main__":
    main()
