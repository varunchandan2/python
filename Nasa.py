# This program will take three time inputs for computation
# If at least two computation values are same it will display the computaion result else will discard it

try:
    comp1 = float(input('Enter the time for computation #1: '))
    comp2 = float(input('Enter the time for computation #2: '))
    comp3 = float(input('Enter the time for computation #3: '))

except:
    print("ERROR, Please enter numbers only")

else:
    if comp1 == comp2:
      print (comp1)
    elif comp2 == comp3:
        print (comp2)
    elif comp3 == comp1:
        print (comp3)
    else:
        print("Computation is discarded")
    
    
    
