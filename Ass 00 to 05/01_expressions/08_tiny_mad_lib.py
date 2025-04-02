# 07_tiny_mad_lib

# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into 
# the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence
# (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Define the sentence start
SENTENCE_START: str = "I never expected to see a"
SENTENCE_END: str = "in front of me!"

def main():
# Get user inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    
    # Construct the sentence
    sentence = f"{SENTENCE_START} {adjective} {noun} suddenly {verb} {SENTENCE_END}"
    
    # Print the sentence
    print(sentence)
    
# Call the main function
if __name__ == "__main__":
    main()
