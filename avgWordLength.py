# this program will calculate the average word length 
try:
    sentence = input("Please enter a long sentence")

except:
    print("ERROR")

else:
    word = sentence.split()
    data = sentence.split()
    avg = sum(len(word) for word in sentence) / len(sentence)

    print("The average word length in a sentence is", avg)
