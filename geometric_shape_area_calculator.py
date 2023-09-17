#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print("Welcome to the geometric shape area calculator!")
    # User Options
    Circle = 1
    Rectangle = 2
    Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print("Circle = 1" + " " + "Rectangle = 2" + " " + "Triangle = 3")

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input("Select a shape by entering 1, 2, or 3 ", )
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(type(choice) == int)

    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        # TODO: Convert 'radius' to float.
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  
        radius = input("Please enter the radius of the circle: ", )
        radius = float(radius)
        area = (radius * radius * circle_pi)
        print(area)

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula to find the area of a rectangle: length times width
        length = input("Please enter the length of the rectangle: ", )
        width = input("Please enter the width of the rectangle: ", )
        length = float(length)
        width = float(width)
        area = (length * width)
        print(area)

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The formula to find the area of a Triangle: half times base times height
        base = input("Please enter the base of the triangle: ", )
        height = input("Please enter the height of the triangle: ", )
        base = float(base)
        height = float(height)
        area = (0.5 * base * height)
        print(area)

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print("Invalid choice .")
    
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    statement ="""Step 1: Find the assignment posted on Canvas/Courseworks
        Step 2: Click on the link to create the repository on GitHub
        Step 3: Clone the repository to your local machine via VS Code using git clone and pasting the link from GitHub
        Step 4: Follow the instructions outline in the ReadMe file and within the working file in order to successfully complete the assignment
        Step 5: Run the code using python3 file_name to ensure that the code runs as expected
        Step 6: Run the unit test via python3 -m unittest and make sure it passes all the tests
        Step 7: Use git add, git commit, and git push to push the assignment back to GitHub to be checked
        Step 8: Copy the GitHub link and take a screenshot of the successful terminal output and submit the course via the assignment on Canvas/Courseworks"""
    print(statement)

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
