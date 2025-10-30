#kujutis nr 7
#Laura Kõrtsmann
#ITS25

import turtle

turtle.speed(2)
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()

for i in range(8):
    turtle.forward(25)
    turtle.right(45)

for i in range(1):
     turtle.forward(25)

for i in range(8):
     turtle.left(90)
     turtle.forward(65)
     turtle.left(90)
     turtle.forward(25)
     turtle.left(90)
     turtle.forward(65)
     turtle.left(90)
     turtle.forward(25)
     turtle.right(45)
     turtle.forward(25)
 
turtle.done()