# Control Flow for Console
# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python.
# To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent.
# You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), 
# you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

import random

# 🎯 Milestone 1: Generate random numbers for player & computer
NUM_ROUNDS = 5  # Number of rounds to play

def play_round(round_num, score):
    """Plays a single round of the High-Low game."""
    
    # Step 1: Generate random numbers
    player_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)

    print(f"\n🔹 Round {round_num}")
    print(f"Your number: {player_num}")

    # 🎯 Milestone 2: Get user input (Higher or Lower)
    while True:
        user_guess = input("Do you think your number is (H)igher or (L)ower? ").strip().upper()
        if user_guess in ["H", "L"]:
            break
        print("❌ Invalid input! Please enter 'H' for Higher or 'L' for Lower.")

    # 🎯 Milestone 3: Game Logic - Determine winner
    if (user_guess == "H" and player_num > computer_num) or (user_guess == "L" and player_num < computer_num):
        print("✅ You guessed correctly! 🎉")
        score += 1  # Increase score
    else:
        print("❌ Wrong guess! The computer wins this round.")
    
    print(f"Computer's number: {computer_num}")
    print(f"Your current score: {score}")

    return score  # Return updated score

# 🎯 Milestone 4: Play multiple rounds
def main():
    """Main function to play the High-Low game."""
    print("🎮 Welcome to the High-Low Game! 🎮")

    score = 0  # Initialize score

    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)
        print("\n" + "=" * 30)  # Separator for readability

    # 🎯 Milestone 5: Add a points system & final message
    display_final_message(score)

# 🎯 Milestone 6: Conditional ending messages
def display_final_message(score):
    """Displays a final message based on performance."""
    print(f"\n🏆 Game Over! Your final score: {score} / {NUM_ROUNDS}")

    if score == NUM_ROUNDS:
        print("🎉 Wow! You played perfectly! 🚀")
    elif score >= (NUM_ROUNDS // 2):  # Won at least half the rounds
        print("👏 Good job, you played really well! 😊")
    else:
        print("💡 Better luck next time! Keep practicing! 🔄")

if __name__ == "__main__":
    main()
