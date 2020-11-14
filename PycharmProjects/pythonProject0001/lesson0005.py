import turtle
import random
turtle.shape("triangle")
turtle.hideturtle()
turtle.forward(0)
turtle.speed(0)
x = 2
a = 13

for i in range(1, 2000):

    turtle.forward(x)
    turtle.left(a)
    turtle.forward(x-random.randint(1, 16))
    turtle.left(a+(random.randint(-15, 15)))
    x = (x + 1)/5





turtle.exitonclick()
