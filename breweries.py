# This program will count the number of breweries in NY and list/write them in a new file



# Throw an exception to check if the file is valid and if so then open the file
try:
    file = open('breweries_us.txt', 'r')
    file2 = open('breweries_ny.txt', 'w')
  
except:
    print("ERROR, Cannot open the file")

else:
    counter = 0

# Now we will split each words in the line into fields called brewery name , type of brewery and state of brewery    
    for line in file:
        for word in line:
            word = line.split()
            brewery_name = word[0]
            type_of_brewery = word[1]
            state_of_brewery = word[2]

# We will check if the state is New York and count the number of breweries and list/write them in a new file
        if state_of_brewery == 'new-york' :
            counter = counter + 1
            file2.write(line)
            
    print("Number of breweries in NY: ", counter)
    
    file2.close()        
    file.close()

# Finally, reading the file where we listed all the breweries in New York
    writeFile  = open('breweries_ny.txt', 'r')
    breweries = writeFile.read()
    print(breweries)
    writeFile.close()

   
    
