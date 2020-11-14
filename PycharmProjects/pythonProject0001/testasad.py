import turtle
turtle.pendown()
side = int(input("Enter the length of the side of the square: "))
color = input("Enter the color name: ")
turtle.fillcolor(color)
turtle.begin_fill()
turtle.pencolor(color)
for _ in range(4):
    turtle.forward(side)
    turtle.left(90)
turtle.right(90)
turtle.end_fill()
turtle.exitonclick()
