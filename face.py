#The graphics library used and new graphics window
from graphics import *
newWin = GraphWin()


#Draw a circle
center = Point(100,100)
lightPinkCircle = Circle(center, 75)
lightPinkCircle.setFill('lightpink')
lightPinkCircle.draw(newWin)

#Draw a circle
center = Point(75,75)
blackCircle = Circle(center, 20)
blackCircle.setFill('black')
blackCircle.draw(newWin)

#Draw a circle
center = Point(125,75)
blackCircle = Circle(center, 20)
blackCircle.setFill('black')
blackCircle.draw(newWin)

#Draw a line
aLine = Line(Point(150,100), Point(100,100))
aLine = Line(Point(100,75), Point(100,100))
aLine.draw(newWin)

#Draw a rectangle
aRectangle = Rectangle(Point(125,115), Point(75,125))
aRectangle.setFill('red')
aRectangle.draw(newWin)



newWin.getMouse()
newWin.close()
