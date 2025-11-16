#Harjutus3

#Infoallikas: https://metshein.com/courses/python-ja-turtle-graphics/lessons/kontrollstruktuurid-if-elif-else-ulesanne-05/
#https://metshein.com/courses/python-ja-turtle-graphics/lessons/funktsioonide-loomine-ulesanne-11/
#https://metshein.com/courses/python-ja-turtle-graphics/lessons/votame-kasutusele-tsuklid-while-ulesanne-10/
#Lisaks vaatasin githubist eelnevaid töid mis tegeime ja sain ka sealt abi
#Lisaks kasutasin teise õpilase abi algul aga edasi proovisin üksi asju muuta



import turtle
import random



def joonista_ruut():
    for _ in range(4):
        turtle.forward(60)
        turtle.right(90)

def joonista_ring():
    turtle.circle(30)

def joonista_viisnurk():
    for _ in range(5):
        turtle.forward(50)
        turtle.right(72)

def joonista_suvaline():

    kujund = random.choice(["ruut", "ring", "viisnurk"])
    if kujund == "ruut":
        joonista_ruut()
    elif kujund == "ring":
        joonista_ring()
    else:
        joonista_viisnurk()
        
    turtle.penup()
    turtle.goto(random.randint(-300,300), random.randint(-300,300))
    turtle.pendown()

while True:
    valik = input("Kujund (viisnurk, ring, ruut, suvaline)? ").lower()
    if valik == "":
        print("Joonistamine lõpetada!")
        break
    arv = int(input("Mitu kujundit? "))
     

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
    jätka = input("Soovid jätkata? Ei soovi jätkata, jäta vastus tühjaks ja kui soovid vajuta Enter: ")
    if jätka.strip() == "":
        print("Joonistamine lõpetada!")
    break    






turtle.done()



