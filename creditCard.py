# This program will accept 16 digits from the user and emits the name of the card's brand
# It performs exception handling
try:
    credit = int(input('Please enter 16 digit credit card number: '))
  
except:
    print("Please enter numeric digits")
     
else:

# This will convert int to string and check for the condition    
    credit = str(credit)
    
    if len(credit)!= 16:
        print("ERROR, Please enter 16 digit numbers")
    elif credit[0] == '4':
        print("It's a Visa card")
    elif credit[0] == '5':
        print("It's a MasterCard")
    elif credit[0] == '6':
        print("It's a Discover card")
    else:
        print("Unknown card")
    
