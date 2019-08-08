import turtle
turtle.shape("turtle")
turtle.hideturtle()
turtle.ht()
turtle.forward(0)
turtle.speed(0)
x = 100
a = 1

for i in range(1, 2500):

    turtle.forward(x)
    turtle.left(a)
    turtle.left(100)

turtle.exitonclick()
turtle.ht()