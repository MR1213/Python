import turtle
turtle.shape("turtle")
turtle.hideturtle()
turtle.ht()
turtle.forward(0)
turtle.speed(0)
x = 30
a = 100

for i in range(1, 250):

    turtle.forward(x)
    turtle.left(a)
    turtle.left(200)

turtle.exitonclick()
turtle.ht()