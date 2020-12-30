# This program will count the number of wineries in California and New York and print the count



# Throw an exception to check if the file is valid and if so then open the file
try:
    file = open('wineries_us.txt', 'r')
    
  
except:
    print("ERROR, Cannot open the file")

else:
    counter = 0
    count = 0

# Now we will split each words in the line into fields    
    for line in file:
        for word in line:
            word = line.split()
            Winery_Name = word[0]
            State = word[1]
            

# We will check if the state is California 'CA' and New York 'NY' and count the number of wineries and print the count
        if State == 'CA':
            counter = counter + 1
        elif State  == 'NY':
            count = count + 1
            
    print("There are", counter,"number of breweries in California ")      
    print("There are", count,"number of breweries in New York ")
    
            
    file.close()

