# Program to calculate the time to travel the distance and speed given by the user
# Using simple Graphics User Interface

from graphics import *

def main():
    win = GraphWin("Time calculator to travel to a destination", 700, 500)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

# Designing the logo
    center = Point(2.5,3.5)
    lightPinkCircle = Circle(center, 0.3)
    lightPinkCircle.setFill('lightpink')
    lightPinkCircle.draw(win)

    center = Point(2.5,3.5)
    yelloCircle = Circle(center, 0.2)
    yelloCircle.setFill('yellow')
    yelloCircle.draw(win)

    logo = Text(Point(2.5,3.5), "Travellers")
    logo.setStyle("bold italic")
    logo.draw(win)

    
# Draw the interface
    Text(Point(.5,3.5), "Distance to travel in miles:").draw(win)
    Text(Point(.5,3.0), "Average speed in miles-per-hour(MPH):").draw(win)
    Text(Point(1,1), "Number of hours to reach the destination:").draw(win)
    

    distanceInput = Entry(Point(1.5,3.5), 5)
    distanceInput.setText("0")
    distanceInput.draw(win)

    speedInput = Entry(Point(1.5,3.0), 5)
    speedInput.setText("0")
    speedInput.draw(win)

    timeOutput = Text(Point(1.6,1),"")
    timeOutput.draw(win)

    button = Text(Point(1.5,2.0), "Calculate the percentage")
    button.draw(win)

    Rectangle(Point(1,1.7), Point(2,2.2)).draw(win)
# Wait for a mouse click
    win.getMouse()
    
# Calculating the time 
    distance = int(distanceInput.getText())
    speed = int(speedInput.getText())
    time = distance/speed
    
# Display output and change button
    timeOutput.setText(time)
    button.setText("Quit")
# wait for click and then quit
    win.getMouse()
    win.close()
    
main()
