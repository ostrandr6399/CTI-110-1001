#Calculate amount a person earns if salary is one penny a day
#6/19/17
#CTI-110-M4HW4_7
#R.Ostrander

NofDays = int(input('How many days do you want to calculate for?' ))

for day in range (NofDays):
    print ('day', day + 1)

    pennies = 2**day
    print ("This would be your Salary if you earned a penny a day", pennies/100)
