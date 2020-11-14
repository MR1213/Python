import turtle

turtle.shape("turtle")
turtle.hideturtle()
turtle.ht()

turtle.speed(0)
x = 1
a = 121

for i in range(1, 1000):

    turtle.forward(x)
    turtle.left(a)
    x = (x + 1)

turtle.exitonclick()
turtle.ht()
