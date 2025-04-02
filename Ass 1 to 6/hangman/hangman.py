# Welcome to Hangman!
# In this game, the computer will randomly select a word, and you have to guess the letters of the word.
# You have a limited number of incorrect guesses before the game is over.
# Try to guess the word before you run out of attempts!

import random

# List of possible words for the game
words = ['python', 'java', 'computer', 'hangman', 'programming', 'developer', 'keyboard']

# Function to display the current state of the word with blanks
def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

# Function to handle the main hangman game logic
def hangman():
    word = random.choice(words)  # Select a random word from the list
    guessed_letters = []  # List to store the guessed letters
    attempts_left = 6  # Number of incorrect guesses allowed
    guessed_correctly = False  # Flag to track if the word is guessed correctly
    
    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {attempts_left} attempts remaining.")
    
    while attempts_left > 0 and not guessed_correctly:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")
        
        # Ask for the user's guess
        guess = input("Enter a letter: ").lower()
        
        # Check if the user entered a valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only a single letter.")
            continue
        
        # Check if the letter was guessed before
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, the letter '{guess}' is not in the word.")
        
        # Check if the user has guessed all letters correctly
        if all(letter in guessed_letters for letter in word):
            guessed_correctly = True
    
    # End the game and show the result
    if guessed_correctly:
        print(f"\nCongratulations! You've guessed the word '{word}' correctly!")
    else:
        print(f"\nSorry, you've run out of attempts! The word was '{word}'.")

# Start the game
if __name__ == "__main__":
    hangman()
