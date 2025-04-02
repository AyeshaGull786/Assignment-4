#In this game, you will choose one of the following options, rock, paper, scissor. you will play against computer
import random

# Function to display the rules of the game
def display_rules():
    print("Welcome to Rock, Paper, Scissors!")
    print("In this game, you will choose one of the following options:")
    print("- Rock (r)")
    print("- Paper (p)")
    print("- Scissors (s)")
    print("You will play against the computer.")
    print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("Let's begin!\n")

# Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['r', 'p', 's'])

# Function to determine the winner of the round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the score
def update_score(winner, score):
    if winner == "You win!":
        score['user'] += 1
    elif winner == "Computer wins!":
        score['computer'] += 1
    # No score update for ties

# Function to play the game
def play_game():
    score = {'user': 0, 'computer': 0}  # Initialize score dictionary
    rounds = 0
    
    display_rules()
    
    while True:
        # Ask the user if they want to continue playing
        play_again = input("Do you want to play a round? (y for Yes, n for No): ").lower()
        if play_again == 'n':
            print(f"\nThanks for playing! Final Score: You: {score['user']} | Computer: {score['computer']}")
            break
        
        rounds += 1
        print(f"\nRound {rounds}:\n")
        
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Print the choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)
        print(winner)
        
        # Update the score
        update_score(winner, score)
        
        # Display current score
        print(f"Current Score: You: {score['user']} | Computer: {score['computer']}\n")

# Start the game
if __name__ == "__main__":
    play_game()
