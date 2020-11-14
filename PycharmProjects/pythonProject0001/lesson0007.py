import turtle, random
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
turtle.shape("turtle")
turtle.hideturtle()
turtle.pensize(10)
turtle.speed(0)
color = random.choice(colors)
turtle.penup()
turtle.goto(0,-90)
turtle.pendown()
for count in range(300000):
    color = random.choice(colors)
    turtle.pencolor(color)
    for i in range(360):
        turtle.forward(2)
        turtle.left(1)


turtle.exitonclick()
turtle.ht()






