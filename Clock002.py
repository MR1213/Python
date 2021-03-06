import turtle
import time


def hand(angle):
    pc = turtle.pencolor()
    bc = turtle.bgcolor()
    turtle.right(angle)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pendown()
    turtle.forward(200)
    time.sleep(1)
    turtle.pencolor(bc)
    turtle.right(180)
    turtle.forward(200)
    turtle.left(180 + angle)
    turtle.pencolor(pc)


hand(0)
hand(6)
hand(12)

# turtle.pensize(1)
# turtle.hideturtle()
# turtle.speed(0)
# turtle.shape("turtle")
# turtle.pendown()
# turtle.forward(200)
# time.sleep(1)
# turtle.pencolor("white")
# turtle.pensize(10)
# turtle.right(180)
# turtle.forward(200)
#
# turtle.pensize(1)
# turtle.pencolor("black")
# turtle.right(6)
# turtle.pendown()
# turtle.forward(200)
# time.sleep(1)
# turtle.pencolor("white")
# turtle.pensize(10)
# turtle.right(180)
# turtle.forward(200)
# turtle.exitonclick()
#
# turtle.pensize(1)
# turtle.pencolor("black")
# turtle.right(12)
# turtle.pendown()
# turtle.forward(200)
# time.sleep(1)
# turtle.pencolor("white")
# turtle.pensize(10)
# turtle.right(180)
# turtle.forward(200)
#
# turtle.pensize(1)
# turtle.pencolor("black")
# turtle.right(18)
# turtle.pendown()
# turtle.forward(200)
# time.sleep(1)
# turtle.pencolor("white")
# turtle.pensize(10)
# turtle.right(180)
# turtle.forward(200)

turtle.exitonclick()
