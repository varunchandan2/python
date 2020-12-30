# This library helps for mathematical calculations
import math

#Input the user for height and angle and accept it as a float
height = input("Enter the height (in km) for the missile: ")
height = float(height)
angle =  input("Enter the angle for the missile: ")
angle = float(angle)

#Conversion of degree to radian

radians = (math.pi/180) * angle

# Calculating the distance

distance = height/ math.sin(radians)

# Displaying the final result

print (" The distance in km is ", distance)
