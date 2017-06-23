# Compute area of a Rectangle
# 12/6/17
# CTI-110 M3T1 - Areas of Rectangles
# Ostrander
#

# demensions of first rectangle
length1 = int(input ('Enter the length of rectangle1: ')) 
width1 = int(input ('Enter the width of rectangle1: '))
# demensions of second rectangle
length2 = int(input ('Enter the length of rectangle2: '))
width2 = int(input ('Enter the length of rectangle2: '))
# Calculate
area1 = length1 * width1
area2 = width2 * length2
# which is bigger
if area1 > area2:
    print ('Rectangle 1 has the greater area.')
elif area2 > area1:
    print ('Rectangle 2 has the greater area.')
else:
    print ('Both have the same area.')
