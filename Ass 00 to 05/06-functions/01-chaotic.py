# 01_chaotic_counting.
# Problem Statement
# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function 
# which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check 
# if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the 
# chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you
# -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.


import random

DONE_LIKELIHOOD = 0.2  # 20% chance of stopping at each number

def done():
    """
    Returns True with a probability of DONE_LIKELIHOOD.
    Otherwise, returns False.
    """
    return random.random() < DONE_LIKELIHOOD  # 20% chance of returning True

def chaotic_counting():
    """
    Prints numbers from 1 to 10 but stops randomly based on done() function.
    """
    for i in range(1, 11):  # Loop from 1 to 10
        if done():  # Check if we should stop
            return  # Exit function if done() returns True
        print(i)  # Print the current number

def main():
    """
    Calls chaotic_counting and then prints "I'm done."
    """
    chaotic_counting()
    print("I'm done.")  # Only prints after chaotic_counting() finishes

if __name__ == '__main__':
    main()
