import turtle
import random

       
def joonista_ruut() :
    for i in range(4) :
        turtle.forward(100)
        turtle.right(90)
       
def joonista_ring() :
    turtle.cirle(100)
   
def joonista_viisnurk() :
    for i in range(5) :
        turtle.forward(100)
        turtle.right(72)
       
def joonista_suvaline() :
    kujund = random.choice(["ruut", "ring", "viisnurk"])
    if kujund == "ruut":
        joonista_ruut()
    elif kujund == "ring":
        joonista_ring()
    else:
        joonista_viisnurk()
       
while True:
    valik = input("Kujund (viisnurk, ring, ruut, suvaline)? ").lower()

    if valik.strip() == "":
        print("Joonistamine lõpetada!")
        break

    arv = int(input("Mitu kujundit soovid joonistada? "))

    for i in range(arv):

        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
    
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        if valik == "ruut":
            joonista_ruut()
       
        elif valik == "ring":
            joonista_ring()
        elif valik == "viisnurk":
            joonista_viisnurk()
        elif valik == "suvaline":
            joonista_suvaline()

        else:
            print("Tundmatu valik")
   
    jätka = input("Soovid jätkata? Kui te ei soovi jätkata, jäta vastus tühjaks ja vajuta klahvi Enter: ")
    if jätka.strip() == "":
        print("Rohkem ei joonista!")
    break
   
turtle.done()
        
    
        
