# 06_rolldice

# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random  # Import the random module to generate random numbers

# Number of sides on each die to roll
TOTAL_SIDES: int = 6

def main():
     #"""Simulates rolling two dice and prints their values and total."""
    die1 = random.randint(1, TOTAL_SIDES)  # Roll first die (1 to 6)
    die2 = random.randint(1, TOTAL_SIDES)  # Roll second die (1 to 6)
    
    # Calculate the sum to get total
    total: int = die1 + die2
    
    # Print the results
      # Print out the results
    print("Dice have", TOTAL_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)
    
#call the main function
if __name__ == '__main__':
    main()