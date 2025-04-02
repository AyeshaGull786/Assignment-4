# 00_averages.

# Problem Statement
# Write a function that takes two numbers and finds the average between the two.

def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b.
    """
    return (a + b) / 2  # Calculate and return the average


def main():
    """
    Takes user input for two numbers, calculates their average,
    then calculates an additional average based on user input.
    """
    # Taking input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Calculate the first average
    avg_1 = average(num1, num2)
    print(f"First Average ({num1} & {num2}):", avg_1)

    # Taking input for another number
    num3 = float(input("Enter third number: "))

    # Calculate the second average
    avg_2 = average(num2, num3)
    print(f"Second Average ({num2} & {num3}):", avg_2)

    # Find the average of both calculated averages
    final = average(avg_1, avg_2)
    print("Final Average:", final)


# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
