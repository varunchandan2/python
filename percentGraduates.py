graduate = input("Enter the number of graduate student in the class: ")
graduate = int(graduate)
underGraduate = input("Enter the number of undergraduate in the class: ")
underGraduate = int(underGraduate)
total = graduate + underGraduate
gradPercent = (graduate/total)*100
gradPercent = float(gradPercent)
ugradPercent = (underGraduate/total)*100
ugradPercent = float(ugradPercent)
print("Number of graduate students in the class is",gradPercent,"%")
print("Number of undergraduate students in the class is",ugradPercent,"%")
      

