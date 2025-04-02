# 01_add_many_number

# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):
    """
    Takes a list of numbers and returns their sum.
    """
    return sum(numbers)

# Example usage
numbers_list = [13, 21, 30, 44, 54, 78]
result = sum_of_numbers(numbers_list)
print("The sum of the numbers is:", result)
