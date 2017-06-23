import turtle          
win = turtle.Screen()  
t = turtle.Turtle()
win.bgcolor("blue")

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("white")     # set pencolor (takes string)
t.shape("turtle")

def branch():
    for i in range(3):
          for i in range(3):
              t.forward(30)
              t.backward(30)
              t.right(45)
          t.left(90)
          t.backward(30)
          t.left(45)
    t.right(90)
    t.forward(90)
for i in range(8):
    branch()
    t.left(45)

win.mainloop()
