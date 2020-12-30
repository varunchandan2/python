# this program will calculate the number of words in the file

try:
    fileName = input("please enter the file name: ")
    file1 = open(fileName)

except:
    print("unable to open the file")
else:
    
    words = file1.read()
    word = words.split()
    length = len(word)
       
    print('Number of words: ', length)
        
    file1.close()
        
        
