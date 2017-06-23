# talying Bugs
# 6/15/17
# CTI-110 M4HW1 - Calories Burned
# R. Ostrander


TotalCalories = 0

TimeInMin= int(input("How many minutes did you spend on the treadmill?  "))



for TimeInMin in range (10,35 ,5):
    TotalCalories = 4.2 * TimeInMin
    print ("At",TimeInMin, "you burned this many calories", TotalCalories)
