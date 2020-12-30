# This application will take pre-order bagel and coffee from Bonnie's Best Bagels
# It will ask for the user name and the order and will give the total for their order including 7% sales tax

import math


from graphics import *

def main():
    win = GraphWin("Bonnie's Best Bagels", 900, 900)
    win.setCoords(0.0, 0.0, 7.0, 8.0)
 

# Designing the Bagel
   

    anOval = Oval(Point(5,6), Point(6,6.5))
    anOval.setFill('brown')
    anOval.draw(win)

    anOval1 = Oval(Point(5,6.1), Point(6,6.6))
    anOval1.setFill('brown')
    anOval1.draw(win)
                  

  
    
# Draw the interface
    menu = Text(Point(3.2,7.8), "Bonnie's Best Bagels")
    menu.setSize(30)
    menu.draw(win)

    name = Text(Point(3,7.2),"Please enter your name: ")
    name.setSize(20)
    name.draw(win)
    thankyou = Text(Point(4,1.3), " Thank you for Shopping with us!").draw(win)
    thankyou.setSize(24)



# Interface for Bagel

    bagel = Text(Point(2,6.8), "Bagels")
    bagel.setSize(24)
    bagel.setStyle("bold italic")
    bagel.draw(win)
    
    plain = Text(Point(2,6.4), "Plain Bagel ($1.50):").draw(win)
    plain.setSize(20)
    everything = Text(Point(2,6.2), "Everything Bagel($1.50):").draw(win)
    everything.setSize(20)
    multigrain = Text(Point(2,6), "Multigrain Bagel($1.50):").draw(win)
    multigrain.setSize(20)
    
# Interface for toppings

    topping = Text(Point(2,5.6), "Toppings")
    topping.setSize(24)
    topping.setStyle("bold italic")
    topping.draw(win)
    
    creameCheese = Text(Point(2,5.2), "Creame Cheese($0.50):").draw(win)
    creameCheese.setSize(20)
    butter = Text(Point(2,5), "Butter($0.25):").draw(win)
    butter.setSize(20)
    
# Interface for coffee

    coffee = Text(Point(2,4.6), "Coffee")
    coffee.setSize(24)
    coffee.setStyle("bold italic")
    coffee.draw(win)
    
    regular = Text(Point(2,4.2), "Regular Coffee($1.75):").draw(win)
    regular.setSize(20)
    decaf = Text(Point(2,4), "Decaf Coffee($1.75):").draw(win)
    decaf.setSize(20)

# Name Input

    nameInput = Entry(Point(4.2,7.2), 9)
    nameInput.draw(win)
   
# bagel input

    plainInput = Entry(Point(4,6.4), 3)
    plainInput.setText("0")
    plainInput.draw(win)

    everythingInput = Entry(Point(4,6.2), 3)
    everythingInput.setText("0")
    everythingInput.draw(win)

    multigrainInput = Entry(Point(4,6), 3)
    multigrainInput.setText("0")
    multigrainInput.draw(win)

# topping input

    butterInput = Entry(Point(4,5.2), 3)
    butterInput.setText("0")
    butterInput.draw(win)

    creamCheeseInput = Entry(Point(4,5), 3)
    creamCheeseInput.setText("0")
    creamCheeseInput.draw(win)

# coffee input
    
    regularInput = Entry(Point(4,4.2), 3)
    regularInput.setText("0")
    regularInput.draw(win)

    decafInput = Entry(Point(4,4), 3)
    decafInput.setText("0")
    decafInput.draw(win)

    nameOutput = Text(Point(4,1),"")
    nameOutput.setSize(24)
    nameOutput.draw(win)
    
    display = Text(Point(3,2),"Total amount due:").draw(win)
    display.setSize(20)
    
    totalOutput = Text(Point(4,2),"$")
    totalOutput.setSize(20)
    totalOutput.draw(win)

    button = Text(Point(4,3.25), "Total")
    button.draw(win)

    Rectangle(Point(3,3.5), Point(5,3)).draw(win)

    
# Wait for a mouse click
    win.getMouse()
    

    oName  = nameInput.getText()
    
# Calculating the total order

# calculating the bagel
    bPlain = int(plainInput.getText())
    bEverything = int(everythingInput.getText())
    bMultigrain = int(multigrainInput.getText())

    tplain = float(bPlain*1.5)
    tEverything = bEverything*1.5
    tMultigrain = bMultigrain*1.5

    totalBagel = tplain+tEverything+tMultigrain
    
# calculating the topping order
    tCream = int(creamCheeseInput.getText())
    tButter = int(butterInput.getText())

    totalCream = float(tCream*0.5)
    totalButter = tButter*0.25

    totalToppings = totalCream+totalButter

# calculating the coffee order    

    cRegular = int(regularInput.getText())
    cDecaf = int(decafInput.getText())

    tRegular = float(cRegular*1.75)
    tDecaf = cDecaf*1.75

    totalCoffee = tRegular+tDecaf
    
# calculating the total and adding the tax   
    totalOrder = totalBagel+totalToppings+totalCoffee
    tax = totalOrder*0.07
    finalOrder = totalOrder + tax
    
# Display output and change button
    totalOutput.setText(finalOrder)
    nameOutput.setText(oName)
    button.setText("Quit")
# wait for click and then quit
    win.getMouse()
    win.close()
    
main()
