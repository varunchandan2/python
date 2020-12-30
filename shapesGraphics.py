#The graphics library used
from graphics import *
newWin = GraphWin()

#Draw a rectangle
aRectangle = Rectangle(Point(100,20), Point(150,100))
aRectangle.draw(newWin)

#Draw a line
aLine = Line(Point(30,20), Point(30,100))
aLine.draw(newWin)


#Draw a circle
center = Point(150,150)
redCircle = Circle(center, 20)
redCircle.setFill('blue')
redCircle.draw(newWin)

newWin.getMouse()
newWin.close()
