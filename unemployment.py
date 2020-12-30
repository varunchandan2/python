# This program will ask the user for the educational attainment and will display the median and unemployment rate

print(" Please enter Educational attainment from the following options: ")
print("Doctoral (D), Masters (M), Bachelor's (B), Some college, no degree(N)")
try:
    data = input('Please enter the option:')
except:
    print("ERROR")
else:
    if data  == 'D':
        print("The median pay will be $1,825 and Unemployment rate is 1.6")
    elif data == 'M':
        print("The median pay will be $1,434 and Unemployment rate is 2.1")
    elif data == 'B':
        print("The median pay will be $1,198 and Unemployment rate is 2.2")
    elif data == 'N':
        print("The median pay will be $802 and Unemployment rate is 3.7")
    else:
        print(" Data not available")
        
    
