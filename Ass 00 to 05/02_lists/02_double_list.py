# 02_double_list

# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# Original list of numbers
numbers: list[int] = [8, 6, 9, 5]  # Creates a list of numbers


# Using list comprehension to double each element
doubled_numbers = [number * 2 for number in numbers]

# Output the result
print(doubled_numbers)