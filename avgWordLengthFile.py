# this program will calculate the average number of words in the file

try:
    fileName = input("please enter the file name: ")
    file1 = open(fileName)

except:
    print("unable to open the file")
else:
    count = 0
    total = 0
    
    words = file1.read()
    for word in words.split():
     count = count + 1
     length = len(word)
     total = length + total
     avg = total/count
       
     print('Average Number of words: ', avg )
     break
        
   
        
