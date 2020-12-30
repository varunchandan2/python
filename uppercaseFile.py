# This program will read one file make the data into uppercase and write it on the other file given by the user
fileName = input("Enter the file name: ")
file2Name = input("Enter the file name to write to: ")

# Throw an exception to validate the files and open it
try:
    file = open(fileName, 'r')
    file2 = open(file2Name, 'w')
except:
    print("ERROR, Cannot open the file")

else:

# First we will read the file and make it upper case and store it in the variable 
    line = file.read() 
    line = line.upper()
    
# We will write in the second file and close both the files    
         
    file2.write(line)
    file2.close()
    file.close()

# Re-open the file and print the data
    writeFile  = open(file2Name, 'r')
    data = writeFile.read()
    print(data)
    writeFile.close()
    
    
