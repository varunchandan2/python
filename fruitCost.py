# This program calculates the total cost of purchase of  mangos and avocados
# It also performs exception handling and only accept numbers from users

num_mangos = input("Enter the number of mangos: ")
num_avocados = input("Enter the number of avocados: ")
try:
    num_mangos = int(num_mangos)
    num_avocados = int(num_avocados)

except:
    print("Input error! enter numbers only!")

else:
    cost = (num_mangos * .45) + (num_avocados * .7)
    print("Your purchase cost today is $", cost)
