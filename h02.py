import turtle

#kilpkonna seaded
turtle.speed(0)
ekraan = turtle.Screen()
ekraan.title("Olümpiarõngad - Laura")
ekraan.setup(500,400)
turtle.pensize(6)

#olümpiarõngad

turtle.pencolor("blue")
turtle.penup()
turtle.goto(-105,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("black")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("red")
turtle.penup()
turtle.goto(110,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("yellow")
turtle.penup()
turtle.goto(-55,-50)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("green")
turtle.penup()
turtle.goto(55,-50)
turtle.pendown()
turtle.circle(50)
    
    
    
turtle.done()    