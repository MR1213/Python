import time
import turtle

def hand(trtl, angle):
    ps = trtl.pensize()
    pc = trtl.pencolor()
    bc = turtle.bgcolor()

    trtl.pensize(2)
    trtl.right(angle)
    trtl.hideturtle()
    trtl.speed(0)
    trtl.pendown()
    trtl.forward(100)
    time.sleep(1)
    trtl.pencolor(bc)
    trtl.right(180)
    trtl.forward(100)
    trtl.left(180 + angle)
    trtl.pencolor(pc)
    trtl.pensize(ps)

screen = turtle.Screen()
trtl = turtle.Turtle()
trtl.speed(0)
screen.setup(1000, 1000)
screen.bgcolor('black')
clr = ['red', 'green', 'blue', 'yellow', 'purple']
trtl.pensize(4)
trtl.shape('turtle')
trtl.penup()
trtl.pencolor('red')
m = 0
for i in range(12):
    m = m + 1
    trtl.penup()
    trtl.setheading(-30 * i + 60)
    trtl.forward(150)
    trtl.pendown()
    trtl.forward(25)
    trtl.penup()
    trtl.forward(20)
    trtl.write(str(m), align="center", font=("Arial", 12, "normal"))
    if m == 12:
        m = 0
    trtl.home()
trtl.home()
trtl.setpos(0, -250)
trtl.pendown()
trtl.pensize(10)
trtl.pencolor('blue')
trtl.circle(250)
trtl.penup()
# trtl.setpos(150, -270)
# trtl.pendown()
# trtl.pencolor('olive')

trtl.setpos(0, 0)
for x in range(0, 60):
    angle = -90 + x * 6
    hand(trtl, angle)

turtle.exitonclick()
