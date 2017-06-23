# talying Bugs
# 6/15/17
# CTI-110 M4T1 - Bug Collector
# R. Ostrander


total = 0
for day in range (1, 8):
    print ("enter the number of bugs you caught on each day", day)
    bugs = int(input ())
    total += bugs
print ( "This is how many bugs you've caught:", total)
