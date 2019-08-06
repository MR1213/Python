import turtle
turtle.shape("turtle")
turtle.hideturtle()
turtle.ht()
turtle.forward(25)
turtle.speed(0)
x = 100
a = 91

for i in range(1, 250):

    turtle.forward(x)
    turtle.left(a)
    turtle.left(10)

turtle.exitonclick()
turtle.ht()