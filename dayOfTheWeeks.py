#This program will display the day of the week entered in number 1 to 7 from the user

finalDay = ""
print('Please enter a number between 1 to 7 to see the corresponding day of the week:')
for num in range(1):
 day = input("Please enter the number: ")
 day = int(day)
# This function will take the input and according to the number will display the day of the week and if it is not in the range will display error 
 if day == 1:
    week = 'Monday'
 elif day == 2:
     week = 'Tuesday'   
 elif day == 3:
    week = 'Wednesday'
 elif day == 4:
    week = 'Thursday'
 elif day == 5:
    week = 'Friday'
 elif day == 6:
    week = 'Saturday'
 elif day == 7:
    week = 'Sunday'
 else:
    week = 'Error the number should be in the range'

 finalDay = finalDay + week   
# this will display the output
print("The day of the week is:", finalDay)
    
          
    
    
  
