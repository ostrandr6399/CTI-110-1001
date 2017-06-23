#hour to minutes
#with formatting
#CTI 110
#R. Ostrander
#6/7

#convert minutes to hh:mm format
minutes = int(input('Please enter the total time in minutes it took: '))
#print = ("YOU entered = str (minutes) + "minutes. ")

# calculate hours
hours = minutes // 60

# calculate the remaining minutes
minutes_remaining = (minutes // 60) % 60

# print how long it took
print ("It took", hours, "hrs", "and", minutes_remaining, "minutes")


