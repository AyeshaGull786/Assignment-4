# Welcome to the 'Guess the Number' game! 
# In this game, I (the computer) will think of a number between 1 and 100,
# and you will try to guess it. After each guess, I will tell you if it's too high, too low, or correct.

def user_guess():
    # Computer randomly selects a number between 1 and 100
    import random
    secret_number = random.randint(1, 100)
    
    print("I have thought of a number between 1 and 100. Try to guess it!")
    
    # Initialize the user's guess and attempts counter
    guess = None
    attempts = 0
    
    # The loop continues until the user guesses correctly
    while guess != secret_number:
        # Ask the user to make a guess
        while True:  # Loop to ensure valid input
            try:
                guess = int(input("\nEnter your guess: "))
                break  # If the input is valid, break the loop
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        attempts += 1
        
        # Provide feedback based on the user's guess
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break  # End the game once the user guesses correctly

# Start the game by calling the function
user_guess()
