# This program will ask the user to guess my favorite number
# It will indicate the user if they are guessing higher/lower then my favorite number


favoriteNumber = 9
guessedNumber = 0
count = 0


while guessedNumber != favoriteNumber:
    try:
        guessedNumber = int(input(" What's my favorite number? "))
    except:
        print("ERROR! Please enter numeric value")
    else:
        count = count + 1
        if guessedNumber == favoriteNumber:
            print("You finally got in", count, "tries!")
            break
        elif guessedNumber > favoriteNumber:
            print("You have to guess lower! ")
        elif guessedNumber < favoriteNumber:
            print ("You have to guess higher! ")
            
