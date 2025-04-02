# 07_tiny_mad_lib

# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into 
# the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence
# (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Function to get user input and ensure it is not empty
def get_input(prompt):
    """
    Prompts the user for input until they provide a non-empty response.
    """
    while True:
        response = input(prompt).strip()  # Ask for input and remove leading/trailing spaces
        if response:  # Check if the input is not empty
            return response
        else:
            print("Error: You cannot leave this field empty. Please enter a valid response.")

# Main function to run the Mad Libs game
def mad_libs():
    """
    This function generates a Mad Libs story based on the user's input. It asks for various types of words 
    and inserts them into a template to create a fun web development-themed story.
    """
    # Intro to the Mad Libs story
    print("Welcome to the Web Development Mad Libs!")
    print("In this story, you will be filling in words to create a fun web development story. Ready? Let's go!\n")
    
    # Getting inputs from the user and ensuring they are not empty
    noun1 = get_input("Enter a noun: ")
    noun2 = get_input("Enter another noun: ")
    adjective1 = get_input("Enter an adjective: ")
    verb1 = get_input("Enter a verb: ")
    verb2 = get_input("Enter another verb: ")
    noun3 = get_input("Enter a noun: ")
    adjective2 = get_input("Enter another adjective: ")
    adverb1 = get_input("Enter an adverb: ")
    place = get_input("Enter a place: ")

    # Creating the Mad Libs story template using the user inputs
    story = f"""
    Once upon a time in the world of web development, there was a {adjective1} {noun1} that could {verb1} websites at incredible speeds. 
    Every developer dreamed of using this {noun1} to {verb2} their projects. But there was a problem: the {noun2} was broken! 

    To fix this, developers had to gather their {noun3}s and work {adverb1} to make the system {adjective2}. 
    The project was huge, but after several days of coding, the developers finally managed to {verb2} it. They deployed it {adverb1} on the {place}.

    The entire team celebrated their success, knowing that the web was now a little more {adjective2} and {adjective1} thanks to their hard work.
    
    And that, dear friend, is the tale of how web development saved the day!
    """
    
    # Output the final Mad Libs story to the user
    print("\nHere's your Web Development Mad Libs Story:\n")
    print(story)

# Run the Mad Libs game
mad_libs()