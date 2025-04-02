# 05_triangle_perimeter

# Problem Statement
# Prompt the user to enter the lengths of each side of a triangle and then calculate
# and print the perimeter of the triangle (the sum of all of the side lengths).

def main():
     # Prompt the user to enter the three sides of the triangle
    side1: float = float(input("Enter the length of side 1: "))
    side2: float = float(input("Enter the length of side 2: "))
    side3: float = float(input("Enter the length of side 3: "))
    
    
    # Calculate the perimeter
    parameter = side1 + side2 + side3
    
    # Print the result
    print(f"The parameter of the triangle is: {parameter}")
    
#call main function
if __name__ == "__main__":
    main()


    

 


