# Program to calculate the percentage of graduate and undergraduate students in the class
# Using simple Graphics User Interface
from graphics import *

def main():
    win = GraphWin("Class percentage", 700, 500)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
# Draw the interface
    Text(Point(.5,3.5), "Number of graduate students:").draw(win)
    Text(Point(.5,3.0), "Number of undergraduate students:").draw(win)
    Text(Point(1,1), "Total percent of grad students:").draw(win)
    Text(Point(1,0.5), "Total percent of undergrad students:").draw(win)

    graduateInput = Entry(Point(1.5,3.5), 5)
    graduateInput.setText("0")
    graduateInput.draw(win)

    undergraduateInput = Entry(Point(1.5,3.0), 5)
    undergraduateInput.setText("0")
    undergraduateInput.draw(win)

    gradPercentOutput = Text(Point(1.6,1),"")
    gradPercentOutput.draw(win)

    uGradPercentOutput = Text(Point(1.6,.5),"")
    uGradPercentOutput.draw(win)

    button = Text(Point(1.5,2.0), "Calculate the percentage")
    button.draw(win)

    Rectangle(Point(1,1.7), Point(2,2.2)).draw(win)
# Wait for a mouse click
    win.getMouse()
    
# Calculating the perecentage
    graduate = int(graduateInput.getText())
    underGraduate = int(undergraduateInput.getText())
    total = graduate + underGraduate
    gradPercent = float((graduate/total)*100)
    uGradPercent = float((underGraduate/total)*100)
# Display output and change button
    gradPercentOutput.setText("%0.2f" % gradPercent)
    uGradPercentOutput.setText("%0.2f" % uGradPercent)
    button.setText("Quit")
# wait for click and then quit
    win.getMouse()
    win.close()
    
main()






   









