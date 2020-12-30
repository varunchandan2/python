# Ask user for house value at market value and accept as integer
houseValue = input("Enter a house value: ")
houseValue = int(houseValue)
#Convert from market value to assessed value
assessedValue = (houseValue * 0.95) * 100
#Formula for calculating tax
schoolTax = (assessedValue * 0.00075) / 100
# Display the result
print(" County school tax is $",schoolTax)
