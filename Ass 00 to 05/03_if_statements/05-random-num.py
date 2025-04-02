#/05_random_numbers.

#print 10 random numbers in the range 1 to 100.
# Each time you run your program you should get different numbers

# Recall that the python random library has a function randint which returns an integer in the range set by
# the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which 
# could include 1 and could include 6:
# value = random.randint(1, 6)

import random  # Import the random module

# Constants
N_NUMBERS: int = 10   # Number of random numbers to generate
MIN_VALUE: int = 1     # Minimum value of the range
MAX_VALUE: int = 100   # Maximum value of the range

def main():
    """ Generate and print 10 random numbers between 1 and 100 """
    for _ in range(N_NUMBERS):  
        random_number = random.randint(MIN_VALUE, MAX_VALUE)  # Generate a random number
        print(random_number)  # Print the number

# Run the main function
if __name__ == '__main__':
    main()
