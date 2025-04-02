#04_flowing_with_data_structures

#In the information flow lesson, we discussed using a variable storing a number as an example of scope.
# We saw that changes we made to the number inside a function did not stay unless we returned it.
# This is true for what we call immutable data types which include things like numbers and strings.
#However, there are also mutable data types where changes stay even if we don't return anything.
# Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and
# dictionaries within helper functions since their changes stay whether or not you return them.
#To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds
# three copies of the data to the list.
# Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.
#Here is an example run of this program (user input in bold italics):



def add_three_copies(my_list, data):
    for i in range(3):      #set the range/number of copies
        my_list.append(data)    #add copies/element in the end

def main():
    message = input("Enter a message to copy: ")
    my_list = []  # Create an empty list             
    print("List before:", my_list)     # Print the empty list
    add_three_copies(my_list, message)  # Call function to modify the list
    print("List after:", my_list)   # The list now contains three copies of input

#call main function
if __name__ == "__main__":
    main()