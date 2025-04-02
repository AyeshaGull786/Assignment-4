
# Countdown Timer in Python
# Description:
# This program allows the user to enter a time duration (in seconds), 
# and it starts a countdown timer displaying the remaining time in MM:SS format.
# Once the countdown reaches zero, it prints "⏰ Time's up!".

import time  # Import time module for delay


# Function to display a countdown timer
def countdown_timer(seconds):
    """
    Runs a countdown timer from the given seconds down to 0.
    Displays time in MM:SS format and updates it every second.
    """
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert total seconds into minutes and seconds
        print(f"Time Remaining: {mins:02}:{secs:02}", end="\r")  # Overwrites the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Reduce time by 1 second

    print("\n⏰ Time's up!")  # Notify when countdown finishes


# Function to get valid time input from user
def get_time_input():
    """
    Prompts the user to enter the countdown duration in seconds.
    Ensures valid positive integer input.
    """
    while True:
        try:
            seconds = int(input("Enter countdown time in seconds: "))  # Take user input
            if seconds > 0:
                return seconds  # Return valid time
            else:
                print("Please enter a positive number.")  # Handle negative values
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # Handle non-numeric input


# Main function to run the countdown timer
def main():
    """
    Main function to execute the countdown timer.
    Calls input function, starts countdown, and displays output.
    """
    print("⏳ Countdown Timer ⏳")  # Display program title
    total_seconds = get_time_input()  # Get valid input from the user
    print(f"Starting countdown for {total_seconds} seconds...\n")
    countdown_timer(total_seconds)  # Start countdown


# Run the program
if __name__ == "__main__":
    main()
