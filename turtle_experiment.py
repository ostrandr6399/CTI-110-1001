import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(7)            # increase pensize (takes integer)
t.pencolor("dark blue")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees

t.left(90)          
t.forward(175)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)
t.right(90)
t.forward(75)
t.right(180)
t.penup()
t.forward(35)
t.right(60)
t.pendown()
t.forward(117)
t.left(60)
t.penup()
t.forward(75)
t.pendown()
t.left(90)
t.forward(175)
t.right(90)
t.forward(75)
t.right(90)
t.forward(175)
t.right(90)
t.forward(75)

# end commands
win.mainloop()             # Wait for user to close window
