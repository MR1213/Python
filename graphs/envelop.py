import math
import turtle

a = 100
b = 200
c = math.sqrt(a^2 + b^2)
bet = math.tanh(a/b)

turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(bet)
turtle.forward(c)

turtle.exitonclick()