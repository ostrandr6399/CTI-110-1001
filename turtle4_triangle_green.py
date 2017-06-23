import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(7)            # increase pensize (takes integer)
t.pencolor("salmon")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees

t.forward(100)          
t.left(120)            
t.forward(100)
t.left(120)
t.forward(100)
t.right (150)


# end commands
win.mainloop()             # Wait for user to close window
