#arpakutio
import random

print("""Noppasovellus
----------------------""")

uudelleen = True

while uudelleen == True:
    noppa = (random.randint(1, 6))
    print("Heittämäsi lukema on:", noppa)
    print("""----------------------
Haluatko heittää uudellen?""")
    vastaus = input("Vastaa Kyllä(k) Ei(e): ").upper()
    if vastaus == "K":
        print("--------------------------------------")
    elif vastaus == "E":
        uudelleen = False
else:
    print("""----------------------
Kiitos käyttämästä noppasovellusta
Käytäthän sovellusta jatkossakin
Jos huomasit bugin Lähetä viesti ######@gmail.com
----------------------""")





#bonus

#näyttämään alussa mahdollisuudet
#saada näyttämään mikä mahdollisuus että tulee sama tai muu

#super bonus

#saa pelaaja valitsemaan monta sivua nopassa on
#näyttämään alussa mahdollisuudet
#saada näyttämään mikä mahdollisuus että tulee sama tai muu

#ultra super useless bonus
#tee hidastus ennen kuin noppaa heitetään