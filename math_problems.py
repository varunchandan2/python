# This program is a menu of different math problems such as Algebra and geometry which will ask the user to select the option 
# It will create random values and ask the user to solve it and then will display the result

import random


print("Please select an option to solve your math problem :")
print("1. Algebra practice, 2. Geometry practice,3. End practice")

# Throw an exception to verify the file and then open and read from it else give an error
try:
    option = int(input("Please enter the option from 1 to 3: "))

except:
    print("ERROR, Please select a numeric value")


else:
    
# If the option is 1,2 or 3 it will execute the following statements. If any other option is selected it will display an error

# If the user selects the 1 option, it will create random values in the given range and store it in the respective variables

    if option == 1:
        num1 = random.randint(45, 56)
        num2 = random.randint(100,166)
        num3 = random.randint(-11, 11)
        result = num1-num2-num3      

# Then it will display the randomly generate values to the user and asks the user to solve the equation

        print("You have selected Algebra  practice: ")
        print("num1: ", num1)
        print("num2: ", num2)
        print("num3: ", num3)

        user_sol = int(input("What is the result of num1-num2-num3?\n "))

# If the user value is equal to the result it will display the correct message else it will display the answer with wrong solution message

        if user_sol == result:
            print("Your answer is correct!")
        else:
            print("Your answer is not correct and the solution is: ", result)

        

# If the user selects the 2 option, it will create random values in the given range and store it in the respective variables

    elif option == 2:
        side1 = random.randint(45,56)
        side2 = random.randint(10,66)
        side3 = random.randint(18,46)
        perimeter = side1+side2+side3

# Then it will display the randomly generate values to the user and asks the user to solve the equation

        print("You have selected Geometry practice: ")
        print("side1: ", side1)
        print("side2: ", side2)
        print("side3: ", side3)

        user_solution = int(input("What is the perimeter of the triangle with side of lenghts side1, side2, side3?\n "))

# If the user value is equal to the result it will display the correct message else it will display the answer with wrong solution message

        if user_solution == perimeter:
            print("Your answer is correct!")
        else:
            print("Your answer is not correct and the solution is: ", perimeter)

        

        
# If option 3 is selected it will end the program

    elif option == 3:
        print("You have ended your practice")

    
    else:
        print("ERROR, please select from the given options")
        
        
        
        

    
    
