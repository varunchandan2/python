# This application will find a random number from the range given by the user

import math
import random


from graphics import *

def main():
    win = GraphWin("Random Number Calculator", 700, 700)
    win.setCoords(0.0, 0.0, 4.0, 5.0)

                  
# Create the interface
    title = Text(Point(2,4), "Random  Number Calculator")
    title.setSize(30)
    title.draw(win)

    head = Text(Point(2,3),"Please enter the range to find a random number ")
    head.setSize(20)
    head.draw(win)

    minimum = Text(Point(1.5,2.5),"Minimum: ")
    minimum.setSize(20)
    minimum.draw(win)

    maximum = Text(Point(2.5,2.5),"Maximum: ")
    maximum.setSize(20)
    maximum.draw(win)

   
#  input

    minimumInput = Entry(Point(1.9,2.5), 3)
    minimumInput.setText("0")
    minimumInput.draw(win)

    maximumInput = Entry(Point(2.9,2.5), 3)
    maximumInput.setText("0")
    maximumInput.draw(win)

# button
    shape = Rectangle(Point(1.5,1.3), Point(2.5,1.8)).draw(win)
    shape.setFill('yellow')

    button = Text(Point(2,1.5), "Find")
    button.setSize(24)
    button.draw(win)

   

# Wait for a mouse click
    win.getMouse()

    
# After the mouse click to display result
    display = Text(Point(1.2,0.8),"Your random number is ").draw(win)
    display.setSize(20)

    totalOutput = Text(Point(2,0.8),"$")
    totalOutput.setSize(20)
    totalOutput.draw(win)
    

# calculating the random number
    
    minNumber = int(minimumInput.getText())
    maxNumber = int(maximumInput.getText())
    
    result = random.randint(minNumber, maxNumber)

       
# Display output and change button
    totalOutput.setText(result)
    button.setText("Quit")
# wait for click and then quit
    win.getMouse()
    win.close()
    
main()
