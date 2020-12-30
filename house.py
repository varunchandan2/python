#The graphics library used and new graphics window
from graphics import *
newWin = GraphWin()

#Draw a triangle as the hut of the house
aPolygon = Polygon(Point(85,50),Point(10,50),Point(50,10))
aPolygon.setFill('blue')
aPolygon.draw(newWin)

#Draw a circle as a window in the hut
center = Point(50,35)
blackCircle = Circle(center, 10)
blackCircle.setFill('black')
blackCircle.draw(newWin)

#Draw a rectangle front of the house
aRectangle = Rectangle(Point(85,50), Point(10,100))
aRectangle.setFill('brown')
aRectangle.draw(newWin)

#Draw a rectangle as the door of the house
bRectangle = Rectangle(Point(65,75), Point(30,100))
bRectangle.setFill('yellow')
bRectangle.draw(newWin)

#Draw a rectangle as the body of the house
cRectangle = Rectangle(Point(85,50), Point(150,100))
cRectangle.setFill('red')
cRectangle.draw(newWin)


# Draw lines connecting the roof of the house
aLine = Line(Point(50,10), Point(110,10))
bLine = Line(Point(110,10), Point(150,50))
aLine.draw(newWin)
bLine.draw(newWin)

#End of the program
newWin.getMouse()
newWin.close()
