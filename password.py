# Ask user for day in month and accept it as string
dayOfMonth = input("Please enter the day in the month you weere born in 2 digits: ")
dayOfMonth = str(dayOfMonth)

# Ask user for favorute animal and accept it as a string
favoriteAnimal = input("Please enter your favorite animal: ")
favoriteAnimal = str(favoriteAnimal)

# Ask user for first name and accept it as a string
firstName = input("Please enter your first name: ")
firstName = str(firstName)

# Store the second last element from first name as firstLetter 
firstLetter = firstName[-2]
firstLetter = str(firstLetter)

# Store the last element from first name as secondLetter 
secondLetter = firstName[-1]
secondLetter = str(secondLetter)

# Store first three elements from favorite animal as threeAnimalLetter
threeAnimalLetters = favoriteAnimal[0:3]
threeAnimalLetters = str(threeAnimalLetters)

# Store first alphabet from firstName to upperCaseLetter and use .upper() to make ot upper case
upperCaseLetter = firstName[0]
upperCaseLetter = str(upperCaseLetter.upper())

# Store ** in twoAsteriks
twoAsteriks = '**'
twoAsteriks = str(twoAsteriks)

# let's combine all the new variables to create a new password for the user
password = firstLetter + secondLetter + dayOfMonth + threeAnimalLetters + upperCaseLetter + twoAsteriks

# Display the new secure password
print("Your new secure password is",password)
