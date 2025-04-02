#04_how_old_are_they

# Problem Statement
# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and
# ages at the end. The autograder is sensitive to capitalization and punctuation, 
# be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

#This function calculates the ages of five friends and prints them.
def main():
    anton: int= 21          # given age of anton
    beth: int = 6 + anton    # Beth is 6 years older than Anton
    chen: int= 20 + beth    # Chen is 20 years older than Beth
    drew: int = anton + chen        # Drew is as old as Chen's age plus Anton's age
    ethan: int = chen            # Ethan is the same age as Chen
    

# Printing the names and their respective ages
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

if __name__ == '__main__':
    main()