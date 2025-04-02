# 03_fahrenheit_to_celsius

# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the formula:
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    """
    Main function to take user input and display the temperature conversion.
    """
    # Prompt user for Fahrenheit temperature
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert using the function
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Print the formatted result
    print(f"Temperature in Celcius is: {fahrenheit:.1f}F = {celsius:.6f} C")

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    main()
