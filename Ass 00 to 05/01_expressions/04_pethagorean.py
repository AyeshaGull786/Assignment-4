# 04_pythagorean_theorem

# Problem Statement
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle 
# and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry.
# It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). 
# You will probably find math.sqrt() to be useful.

import math  # Import the math module to use sqrt()

def main():
    
    # Get the two side lengths from the user and cast them to be numbers
    ab: float= float(input("Enter the length of first side AB: "))
    ac: float= float(input("Enter the length of second side AC: "))
    
    # Compute the hypotenuse
    hypotenuse: float = math.sqrt(ab**2 + ac**2)             # Using the formula: c² = a² + b²
    
     # Print the result
    print(f"\nThe length of the hypotenuse (BC) is: {hypotenuse:.2f}")
    
# Call main function
if __name__ == "__main__":
    main()

