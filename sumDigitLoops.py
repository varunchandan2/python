# this program will sum the digits in a string
try:
 single_digit = input("Please enter single digit number nothing seperating them")
except:
    print("ERROR")
else:
    sum =0
    for i in single_digit:
     sum = sum + int(i)

    print('The sum of the four numbers is ', sum)
