# DEbugging Lab
# 6/13/17
# CTI-110 M3LAB - Debugging
# R. Ostrander


score = int(input('What was your score? '))

if score >= 90:
    print ("Your grade is A ")
elif score >= 80:
    letterGrade = "B"
    print ("Your grade is B ")
elif score >= 70:
    print ("Your grade is C ")
elif score >= 60:
    print ("Your grade is d")
elif score <= 59:
    print ("You are a loser!")
