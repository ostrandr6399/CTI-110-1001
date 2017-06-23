# CTI 110-1001
# Mr. Norris (Instructor)
# R.Ostrander
# June 20,2017


import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees

for sides in range (2):
    t.forward(100)
    t.left(120)
t.forward(100)
t.right (150)
t.penup()
t.forward(90)
t.pendown()
t.right (90)
t.forward(100)
for sides in range (3):
    t.left(90)
    t.forward(100)

# end commands
win.mainloop()             # Wait for user to close window
