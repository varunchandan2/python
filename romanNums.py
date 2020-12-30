# This program will accept one integer in the range of 1 to 10
# If the number is in the range it will display the roman numeral version

try:
    
     digit = int(input('Please enter one Integer from 1 to 10: '))
except:
    for num in range(1,11):
     print("Error please enter a number ")
else:
    
     if digit == 1:
        print("I")
     elif digit == 2:
        print("II")
     elif digit == 3:
        print("III")
     elif digit == 4:
        print("IV")    
     elif digit == 5:
        print("V")
     elif digit == 6:
        print("VI")
     elif digit == 7:
        print("VII")
     elif digit == 8:
        print("VIII")
     elif digit == 9:
        print("IX")
     elif digit == 10:
        print("X")
     else:
        print("Please enter number in the range")
        
