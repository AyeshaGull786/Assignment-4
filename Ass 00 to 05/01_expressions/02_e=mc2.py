# 02_e=mc2

# Problem Statement
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy 
# equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation.
# You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):
# Enter kilos of mass: 100
# e = m * C^2...
# m = 100.0 kg
# C = 299792458 m/s
# 8.987551787368176e+18 joules of energy! 

#store value of speeed of light
C: int = 299792458

def main():
    mass_in_kg: float = float(input("\nEnter a value of mass in kilo: "))
    
    #now we set data 
    print("\ndata:")
    print("e = m*c^2...")
    print("m = " + str (mass_in_kg)+ " kg")
    print("c = " + str(C) + " m/s")
    
    # using the ** operator to raise C to the power of 2
    #putting values
    energy_in_joules: float = mass_in_kg * (C**2)
    
    # Print the result
    print("\n" + str(energy_in_joules) + " Joules of Energy\n")
    

# Call the main function
if __name__ == '__main__':
    main()
