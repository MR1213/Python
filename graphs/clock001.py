import time
import turtle


def hand(trtl, angle):
    pc = trtl.pencolor()
    bc = trtl.bgcolor()
    trtl.right(angle)
    trtl.hideturtle()
    trtl.speed(0)
    trtl.pendown()
    trtl.forward(200)
    time.sleep(1)
    trtl.pencolor(bc)
    trtl.right(180)
    trtl.forward(200)
    trtl.left(180 + angle)
    trtl.pencolor(pc)