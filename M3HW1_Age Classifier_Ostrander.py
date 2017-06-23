# Age classifier
# 6/14/17
# CTI-110 M3HW1 - Age Classifier
# R. Ostrander
#

age = float(input('How old are you in years? '))
if age >=60:
    print ("you are wise!")
if age >=20 and age <60:
    print ("You are an adult")
elif age >=13 and age <20:
    print ("You are a teenager")
elif age >=1 and age <13:
    print ("You are a child")
if age < 1:
    print ("You are an infant")

