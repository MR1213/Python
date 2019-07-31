# File: Hello.py

# Description: This program writes out Hello World

import turtle


def main():
    # put label on top of page
    turtle.title('Hello World')

    # setup screen size
    turtle.setup(1000, 1000, 0, 0)

    # move turtle to origin
    turtle.penup()
    turtle.goto(0, 0)

    # set the color to navy
    turtle.color('navy')

    # write the message
    turtle.write('Hello World!', font=('Times New Roman', 36, 'bold'))

    # hide the turtle
    turtle.hideturtle()

    # persist the drawing
    turtle.done()


main()

# File: Squares.py

# Description: Draws squares of different sizes

import turtle


# draw a square of a given side
# starting at uuper left corner (x, y)
def drawSquare(ttl, x, y, side):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)  # set the pen in the +ve x direction
    ttl.pendown()
    for iter in range(4):
        ttl.forward(side)
        ttl.right(90)
    ttl.penup()


def main():
    # put label on top of page
    turtle.title('Squares')

    # setup screen size
    turtle.setup(800, 800, 0, 0)

    # create a turtle object
    ttl = turtle.Turtle()

    # assign a color to the turtle object
    ttl.color('red')

    # draw multiple squares
    drawSquare(ttl, -50, -50, 50)
    drawSquare(ttl, 0, 0, 50)
    drawSquare(ttl, 50, 50, 50)
    drawSquare(ttl, -50, 50, 150)

    # fill a closed region
    ttl.fillcolor('purple')
    ttl.begin_fill()
    drawSquare(ttl, 0, 0, 50)
    ttl.end_fill()
    # persist drawing
    turtle.done()


main()

# File: Figures.py

# Description: Draws various types of geometric figures

import turtle, math


# draw a line from (x1, y1) to (x2, y2)
def drawLine(ttl, x1, y1, x2, y2):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.penup()


def drawPolygon(ttl, x, y, num_side, radius):
    sideLen = 2 * radius * math.sin(math.pi / num_side)
    angle = 360 / num_side
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    for iter in range(num_side):
        ttl.forward(sideLen)
        ttl.left(angle)


def main():
    # put label on top of page
    turtle.title('Geometric Figures')

    # setup screen size
    turtle.setup(800, 800, 0, 0)

    # create a turtle object
    ttl = turtle.Turtle()

    # draw equilateral triangle
    ttl.color('blue')
    drawPolygon(ttl, -200, 0, 3, 50)

    # draw square
    ttl.color('red')
    drawPolygon(ttl, -50, 0, 4, 50)

    # draw pentagon
    ttl.color('forest green')
    drawPolygon(ttl, 100, 0, 5, 50)

    # draw octagon
    ttl.color('DarkOrchid4')
    drawPolygon(ttl, 250, 0, 8, 50)

    # draw a line
    ttl.color('gold4')
    drawLine(ttl, -200, -10, 325, -10)
    drawLine(ttl, -200, -15, 325, -15)

    # persist drawing
    turtle.done()


main()

# File: ColorShapes.py

# Description: Draws filled in shapes

import turtle


def main():
    # put label on top of page
    turtle.title('Colorful Shapes')

    # setup screen size
    turtle.setup(800, 800, 0, 0)

    # draw a triangle
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('red')
    turtle.circle(40, steps=3)
    turtle.end_fill()

    # draw a square
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('navy')
    turtle.circle(40, steps=4)
    turtle.end_fill()

    # draw a pentagon
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('green')
    turtle.circle(40, steps=5)
    turtle.end_fill()

    # draw a hexagon
    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('yellow')
    turtle.circle(40, steps=6)
    turtle.end_fill()

    # draw a circle
    turtle.penup()
    turtle.goto(200, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('purple')
    turtle.circle(40)
    turtle.end_fill()

    # write header
    turtle.penup()
    turtle.goto(-100, 50)
    turtle.write('Cool Colorful Shapes', font=('Times', 18, 'bold'))

    # hide turtle
    turtle.hideturtle()

    # persist drawing
    turtle.done()


main()

# File: Func.py

# Description: Draws users defined functions

import math, turtle


# draw a line from (x1, y1) to (x2, y2)
def drawLine(ttl, x1, y1, x2, y2):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.penup()


# write label at location x, y
def labelPoint(ttl, x, y, label):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.write(label)
    ttl.penup()


def drawGridMark(ttl, x, y, isVertical):
    if isVertical:
        drawLine(ttl, x, y + 5, x, y - 5)
    else:
        drawLine(ttl, x - 5, y, x + 5, y)


def labelGridPoint(ttl, x, y, isVertical, text):
    if isVertical:
        labelPoint(ttl, x - 20, y - 20, text)
    else:
        labelPoint(ttl, x + 20, y, text)


def drawGridScaled(ttl):
    # draw the axes
    drawLine(ttl, -400, 0, 400, 0)
    drawLine(ttl, 0, 400, 0, -400)

    # label the x axis
    for x in [-300, -200, -100, 100, 200, 300]:
        drawGridMark(ttl, x, 0, True)
        labelGridPoint(ttl, x, 0, True, (x / 100, 0))

    # label the y axis
    for y in [-300, -200, -100, 100, 200, 300]:
        drawGridMark(ttl, 0, y, False)
        labelGridPoint(ttl, 0, y, False, (0, y / 100))


def drawFnScaled(ttl, fn, lower, upper, step):
    ttl.penup()
    x = lower
    y = fn(x)
    scaledX = x * 100
    scaledY = y * 100
    ttl.goto(scaledX, scaledY)
    ttl.pendown()
    while x < upper:
        x = x + step
        y = fn(x)
        scaledX, scaledY = x * 100, y * 100
        ttl.goto(scaledX, scaledY)
    ttl.penup()


def myFunc(x):
    return (x ** 2 - 4)


def main():
    # put label on top of page
    turtle.title('Graphs of Functions')

    # setup screen size
    turtle.setup(800, 800, 0, 0)

    # create a turtle object
    ttl = turtle.Turtle()

    # draw the grid
    drawGridScaled(ttl)

    # draw sine finction
    ttl.pencolor('red')
    drawFnScaled(ttl, math.sin, -math.pi, math.pi, 0.01)

    # draw cosine function
    ttl.pencolor('blue')
    drawFnScaled(ttl, math.cos, -math.pi, math.pi, 0.01)

    # draw my function
    ttl.pencolor('purple')
    drawFnScaled(ttl, myFunc, -math.pi, math.pi, 0.01)

    # persist drawing
    turtle.done()


main()

# File: RandomWalk.py

# Description: Draws a grid and exhibits a random walk

import turtle, random


def main():
    # put label on top of page
    turtle.title('Random Walk')

    # setup screen size
    turtle.setup(1000, 1000, 0, 0)

    # set turtle speed
    # turtle.speed (1)

    # draw 16 x 16 lattice
    turtle.color('gray')

    # draw horizontal lines
    x = -80
    for y in range(-80, 80 + 1, 10):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(160)

    # draw vertical lines
    y = 80
    turtle.right(90)
    for x in range(-80, 80 + 1, 10):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(160)

    # start random walk
    turtle.pensize(3)
    turtle.color('red')

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    x = y = 0
    while (abs(x) < 80 and abs(y) < 80):
        r = random.randint(0, 3)
        if r == 0:
            x += 10
            turtle.setheading(0)
            turtle.forward(10)
        elif r == 1:
            y -= 10
            turtle.setheading(270)
            turtle.forward(10)
        elif r == 2:
            x -= 10
            turtle.setheading(180)
            turtle.forward(10)
        elif r == 3:
            y += 10
            turtle.setheading(90)
            turtle.forward(10)

            # persist drawing
    turtle.done()


main()

# File: Sierpinski.py

# Description: Draws Sierpinski's Curve or Gasket

import math, turtle


def drawGasket(ttl, size):
    if size < 10:
        return
    for iter in range(3):
        ttl.forward(size / 2)
        insertGasket(ttl, size)
        ttl.forward(size / 2)
        ttl.right(120)


def insertGasket(ttl, size):
    ttl.left(120)
    drawGasket(ttl, size / 2)
    ttl.right(120)


def oneSide(ttl, s, diag, level):
    if (level == 0):
        return
    else:
        oneSide(ttl, s, diag, level - 1)
        ttl.right(45);
        ttl.forward(diag);
        ttl.right(45)
        oneSide(ttl, s, diag, level - 1)
        ttl.left(90);
        ttl.forward(s);
        ttl.left(90)
        oneSide(ttl, s, diag, level - 1)
        ttl.right(45);
        ttl.forward(diag);
        ttl.right(45)
        oneSide(ttl, s, diag, level - 1)


def curve(ttl, s, level):
    diag = s / math.sqrt(2)
    for iter in range(4):
        oneSide(ttl, s, diag, level)
        ttl.right(45)
        ttl.forward(diag)
        ttl.right(45)


def main():
    # put label on top of page
    turtle.title('Recursive Figures')

    # setup screen size
    turtle.setup(1000, 1000, 0, 0)

    # create a turtle object
    ttl = turtle.Turtle()

    # draw the sierpinski curve
    # curve (ttl, 15, 3)

    # draw gasket
    drawGasket(ttl, 200)

    # persist drawing
    turtle.done()


main()

# File: Sun.py

# Description: Draws recursively a sun like figure

import math, turtle


def drawArcR(ttl, size, degrees):
    for iter in range(degrees):
        ttl.forward(size)
        ttl.right(1)


def drawArcL(ttl, size, degrees):
    for iter in range(degrees):
        ttl.forward(size)
        ttl.left(1)


def drawRay(ttl, size):
    for iter in range(2):
        drawArcR(ttl, size, 90)
        drawArcL(ttl, size, 90)


def drawSun(ttl, size, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    for iter in range(9):
        drawRay(ttl, size)
        ttl.right(160)
    ttl.end_fill()


def main():
    # put label on top of page
    turtle.title('Sun Figure')

    # setup screen size
    turtle.setup(1000, 1000, 0, 0)

    # create a turtle object
    ttl = turtle.Turtle()

    # draw the sun figure
    drawSun(ttl, 1, 'red')

    # persist drawing
    turtle.done()


main()
