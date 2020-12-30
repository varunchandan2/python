# this program will count the number of words in a sentence
try:
    phrase = input("Please write a sentence:")

except:
    print("ERROR")
else:

    res = len(phrase.split())

    print("The number of words in sentence is ", str(res))
    
