from turtle import *
turtle = Turtle()
screen = Screen()
screen.onscreenclick(turtle.goto)
screen.listen()
turtle.getscreen()._root.mainloop()

def mousePosition():
    canvas = turtle.getcanvas()
    x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
    turtle.goto(x, y)