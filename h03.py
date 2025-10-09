import turtle

#Harjutus03.1
nimi= "juhan"
vanus = 58
pikkus = 1.80


print(nimi,",", vanus,"aastat vana ja pikkus on", pikkus, "m")
print(nimi+", "+ str(vanus),"aastat vana ja pikkus on "+str(pikkus)+" m")


# Loo muutuja toode, mis sisaldab toote nime (string)
# Loo muutuja kogus, mis näitab, mitu toodet soovitakse osta (integer)
# Loo muutuja hind, mis näitab ühe toote hinda (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soovin porgandeid 3, mille tüki hind on 5.35 eurot.”
# Kasuta väljatrükkimisel ainult plussi (+)

sihtkoht = "Haapsalu"
paevade_arv = 5
oobimise_hind = 100.50
kokku = paevade_arv * oobimise_hind
print(sihtkoht,"reis kestab", paevade_arv,"päeva ja maksab kokku",kokku,"€")


kylje_pikkus = 100
nurk = 90
kujundi_varv = "blue"
x = 110

turtle.pencolor(kujundi_varv)
for i in range(3):
    for i in range(4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    x = x * 2
    


turtle.done()