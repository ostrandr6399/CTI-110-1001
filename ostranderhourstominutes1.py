#hour to minutes
#with formatting
#CTI 110
#R. Ostrander
#6/7

#convert minutes to hh:mm format
minutes = int(input('Number of minutes '))
#print = ("YOU entered = str (minutes) + "minutes. ")
# calculate hours
hours = (minutes // 60) % 60

print ("that is", hours, "hrs")


