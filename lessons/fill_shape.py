import turtle
a=360
b=2
c=1
d=0
turtle.speed(0)
turtle.shape("turtle")
turtle.fillcolor('blue')
turtle.begin_fill()
for i in range(a):
    turtle.forward(b)
    turtle.right(c)
    turtle.left(d)
turtle.end_fill()
turtle.ht()
turtle.exitonclick()


#a-360 b-1 c-1 : circle
#a-4 b-any number c-90 : square
#a-3 b-any number c-120 : triangle
#a=12 b-any number c-45 : hexagon
