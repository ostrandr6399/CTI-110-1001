# Body Mas Index
# 6/13/17
# CTI-110 M3HW2_14
# R. Ostrander

Weight = int(input('How much do you weigh? '))
Height = int(input('How Tall are you? '))
BMI = Weight * 703/Height**2
print ('Your BMI is',BMI)
if BMI >= 25:
    print ("You are considered overweight")
elif BMI >=18.5:
    print ("You are with in standards")
elif BMI <= 18.4:
    print ("You are considered Underwight")



