# 06_is_odd.

# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def even_odd_labels():
    """Prints numbers from 10 to 19 with their even/odd labels."""
    for num in range(10, 20):  # Loop from 10 to 19
        if num % 2 == 0:
            print(num, "even")  # Print even numbers
        else:
            print(num, "odd")   # Print odd numbers

# Run the function
even_odd_labels()
