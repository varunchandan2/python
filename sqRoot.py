# This program will 3 digit number from the user and display the square root if it passes the condition 

try:
    digit = int(input(' Enter three integer: '))

except:
    print("ERROR, PLEASE ENTER NUMERIC DIGITS")
else:
    if( digit>=100 and digit <= 999):
        sqRoot = digit ** 2
        print("The square root is: ", sqRoot)
    else:
         print(" Please enter a three digit number")
        
        
                
