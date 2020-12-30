#This program calculates the account's future value and the number of years money will be in the savings account

#Ask user for account's present value and accept it as a float value
accountPresentValue = input("Please enter the account's present value: ")
accountPresentValue = float(accountPresentValue)

#Ask user for annual interest rate in percentage and accept it as a float value 
annualInterestRate = input("Please enter the annual interest rate percentage: ")
annualInterestRate = float(annualInterestRate)

#Convert the percentage to a decimal number
annualInterestRate = annualInterestRate / 100

#Ask user for number of years to keep in the account and accept as an integer value
numberOfYears = input("Please enter the number of years: ")
numberOfYears = int(numberOfYears)

#Using the formula to calculate future value
futureValue = accountValue * ( 1 + interestRate)**numberOfYears

#Display the future value and number of years they would like to keep in the account
print(" Your saving account's future value is $",futureValue, "and the number of years the money will be in the account is",numberOfYears,"years")
