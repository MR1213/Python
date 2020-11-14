import turtle
turtle.begin_fill()
turtle.shape("triangle")
turtle.hideturtle()
turtle.forward(0)
turtle.speed(0)
x = 2
a = 60

for i in range(1, 2000):
    turtle.forward(x)
    turtle.left(a)
    turtle.forward(36)
    turtle.left(15)
    turtle.fillcolor("green")
    turtle.end_fill()
    x = x+1





turtle.exitonclick()
