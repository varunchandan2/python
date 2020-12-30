# This program will list all the customers last name starting with S from the customers.txt file


#Accept file name from the user
fileName = input("Enter the file name: ")

# Throw an exception to check if the file is valid and if so then open the file
try:
    file = open(fileName, 'r')
  
except:
    print("ERROR, Cannot open the file")

else:

# Now we will split each words in the line into fields called first name , last name and contact    
    for line in file:
        for word in line:
            word = line.split()
            firstName = word[0]
            lastName = word[1]
            contact = word[2]

# We will check if the last name starts with S and print the names
        if lastName.startswith("S"):
            print(lastName)
            
    file.close()
