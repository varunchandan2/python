try:
    user = int(input('Please enter a range of numbers in 4 to 16 weeks: '))
except:
    print("ERROR! Please enter number")
else:
    for num in range(1,17):
        while user < 17:
            if user >= 4 and user <= 6:
                print("Rent cost: $3080")
            elif user >= 7 and user <= 10:
                print("Rent cost: $2650")
            elif user >= 11 and user <= 16:
                print("Rent cost: $2090")
            else:
                print("not in the range")
                
            
    
