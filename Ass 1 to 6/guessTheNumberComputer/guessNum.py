# Welcome to the 'Guess the Number' game! 
# The computer will try to guess the number you're thinking of, between 1 and 100.
# For each guess, you need to provide feedback:
# - Type 'h' if my guess is too high.
# - Type 'l' if my guess is too low.
# - Type 'c' if I guessed correctly.

def computer_guess():
    # Set the initial range
    low = 1
    high = 100
    feedback = ""

    # Tell the user to think of a number
    print("Please think of a number between 1 and 100 and keep it in your mind. I will try to guess it.")

    # The loop continues until the computer guesses correctly
    while feedback != "c":
        # Tell the user that the computer is making a guess
        print(f"\nI'm making a guess...")

        # The computer guesses the middle number in the range
        guess = (low + high) // 2
        print(f"My guess is: {guess}")

        # Provide instructions to the user on what to do next
        print("Please respond with:")
        print("'h' if my guess is too high.")
        print("'l' if my guess is too low.")
        print("'c' if my guess is correct.")

        # Get the feedback from the user
        feedback = input("Your feedback: ").lower()

        # Process the user's feedback
        if feedback == "h":
            high = guess - 1  # Adjust the upper bound
            print("Okay, I'll guess lower next time!")
        elif feedback == "l":
            low = guess + 1  # Adjust the lower bound
            print("Got it! I'll guess higher next time.")
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} correctly!")
        else:
            # Handle invalid feedback
            print("Invalid input. Please respond with 'h', 'l', or 'c'.")

# Start the game by calling the function
computer_guess()
