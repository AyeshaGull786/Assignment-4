# 00_choosing_returns.
# Problem Statement
# There are times where we want to return different things from a function based on some condition. To practice this idea,
# imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). 
# Fill out the is_adult(age) function, which returns True if the function takes an 
# age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

# Define the legal adult age
ADULT_AGE = 18  

def is_adult(age: int) -> bool:
    """Returns True if age is 18 or older, otherwise returns False."""
    return age >= ADULT_AGE  # Directly return True/False based on condition

def main():
    """Gets user input and checks if they are an adult."""
    age = int(input("Enter your age: "))  # Take user input
    if is_adult(age):  
        print("You are an adult!")  # If True, print this
    else:
        print("You are not an adult yet!")  # If False, print this

# Run the program
if __name__ == "__main__":
    main()
