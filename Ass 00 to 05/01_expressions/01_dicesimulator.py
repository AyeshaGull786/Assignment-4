# /01_dicesimulator

# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random     # Import the random module to generate random numbers


# Number of sides on each die to roll
TOTAL_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, TOTAL_SIDES)
    die2: int = random.randint(1, TOTAL_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 20
    print("die1 in main() starts as: " + str(die1))
    
    #Calls roll_dice() three times to simulate three rolls.
    print("\nRolling two dice three times:")
    
    for _ in range(3):  # Loop 3 times
        
        roll_dice()  # Call the roll_dice function

    print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()