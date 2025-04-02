# Intro to python 
# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, 
# has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further
# than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars,
# an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight
# on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. 
# You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded 
# to 2 decimal places which is 3.14.

## 🎯 Milestone 1: Calculate weight on Mars
def calculate_mars_weight(earth_weight):
    """Calculates weight on Mars (37.8% of Earth weight)."""
    mars_weight = earth_weight * 0.378
    return round(mars_weight, 2)

# 🎯 Milestone 2: Calculate weight on any planet
PLANET_GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def calculate_planet_weight(earth_weight, planet):
    """Calculates weight on a given planet using its gravity factor."""
    gravity_factor = PLANET_GRAVITY.get(planet)
    if gravity_factor:
        return round(earth_weight * gravity_factor, 2)
    return None

def main():
    """Main function to get user input and calculate weight."""
    earth_weight = float(input("Enter your weight on Earth (kg): "))

    # 🎯 Milestone 1: Mars weight calculation
    mars_weight = calculate_mars_weight(earth_weight)
    print(f"\n✅ Your weight on Mars would be: {mars_weight} kg")

    # 🎯 Milestone 2: Weight on any planet (user selects from a list)
    print("\nSelect a planet to calculate your weight there (select number):")
    
    planets = list(PLANET_GRAVITY.keys())

    while True:
        # Display options
        for i, planet in enumerate(planets, 1):
            print(f"{i}. {planet}")

        try:
            choice = int(input("\nEnter the number of your chosen planet: "))
            
            if 1 <= choice <= len(planets):
                selected_planet = planets[choice - 1]
                planet_weight = calculate_planet_weight(earth_weight, selected_planet)
                print(f"\n🌍 Your weight on {selected_planet} would be: {planet_weight} kg")
                break  # Exit loop after a valid selection
            else:
                print("❌ Invalid choice. Please select a number from the list.")
        
        except ValueError:
            print("⚠️ Please enter a valid number from the menu.")

if __name__ == "__main__":
    main()
