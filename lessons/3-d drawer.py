from turtle import *

# set a shape and colour
shape("circle")
shapesize(5,1,4)
fillcolor("pink")
pencolor("darkred")

penup() # no drawing
goto(0, -250)

# main draw loop
for i in range(288):
  forward(3)
  left(1.25)
  tilt(15)
  stamp()

exitonclick()