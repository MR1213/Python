import turtle

turtle.shape("turtle")

turtle.forward(25)

x = 100
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

    turtle.left(7)

turtle.exitonclick()