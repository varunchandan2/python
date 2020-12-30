# This file will display the number of customers from the customers.txt file given by the user

fileName = input("Enter the file name: ")

# Throw an exception to validate the file and open it
try:
    file = open(fileName, 'r')
  
except:
    print("ERROR, Cannot open the file")

else:
# Now we will split each words in the line into fields called first name , last name and contact     
    customers = 0 
    for line in file:
        for word in line:
            word = line.split()
            firstName = word[0]
            lastName = word[1]
            contact = word[2]

# We will check if we have all the fields and if so it will count the number and print the total            
        if firstName and lastName and contact:
            customers = customers + 1

    print('Number of customers: ', customers)
        

   
    file.close()

   
