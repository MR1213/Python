import turtle

turtle.shape("turtle")
turtle.hideturtle()
turtle.ht()
turtle.forward(25)
turtle.speed(0)
x = 90
a = 90

for i in range(1, 100):

    turtle.forward(x)
    turtle.left(a)
    turtle.forward(x)
    turtle.left(a)
    turtle.forward(x)
    turtle.left(a)
    turtle.forward(x)
    turtle.left(a)

    turtle.left(123)

turtle.exitonclick()
turtle.ht()