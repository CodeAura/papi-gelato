##................................................................................................................................................................
##.PPPPPPPPPPPPP.....AAAAAAA......AAAPPPPPPPPPP...PPPII.............GGGGGGGGGG....GGGEEEEEEEEEEEE..EELLL.............AAAAAAA.....AAAATTTTTTTTTT...TTOOOOOOOO......
##.PPPPPPPPPPPPPP....AAAAAAA......AAAPPPPPPPPPPP..PPPII...........GGGGGGGGGGGGGG..GGGEEEEEEEEEEEE..EELLL.............AAAAAAA.....AAAATTTTTTTTTT..TTTOOOOOOOOOO....
##.PPPPPPPPPPPPPP....AAAAAAAA.....AAAPPPPPPPPPPPP.PPPII.......... GGGGGGGGGGGGGG..GGGEEEEEEEEEEEE..EELLL.............AAAAAAAA....AAAATTTTTTTTTT.TTTTOOOOOOOOOOO...
##.PPPPP..PPPPPPPP..AAAAAAAAA.....AAAPP...PPPPPPP.PPPII......... GGGGGG.GGGGGGGG.GGGEE............EELLL............AAAAAAAAA.........TTTT.....TTTTTOOO.OOOOOOO...
##.PPPPP....PPPPPP..AAAAAAAAA.....AAAPP.....PPPPP.PPPII......... GGGG.....GGGGG..GGGEE............EELLL............AAAAAAAAA.........TTTT.....TTTTTO.....OOOOOO..
##.PPPPP.....PPPPP..AAAAAAAAAA....AAAPP.....PPPPP.PPPII......... GGG.............GGGEE............EELLL............AAAAAAAAAA........TTTT.....TTTTT.......OOOOO..
##.PPPPP....PPPPPP.PAAAA.AAAAA....AAAPP.....PPPPP.PPPII........ GG..............GGGEE............EELLL...........LAAAA.AAAAA........TTTT....TTTTTT.......OOOOO..
##.PPPPP..PPPPPPPP.PAAAA.AAAAAA...AAAPP...PPPPPPP.PPPII........ GG..............GGGEEEEEEEEEEE...EELLL...........LAAAA.AAAAAA.......TTTT....TTTTT........OOOOO..
##.PPPPPPPPPPPPPP.PPAAAA..AAAAA...AAAPPPPPPPPPPPP.PPPII........ GG....GGGGGGGGG.GGGEEEEEEEEEEE...EELLL..........LLAAAA..AAAAA.......TTTT....TTTTT........OOOOO..
##.PPPPPPPPPPPPP..PPAAA...AAAAA...AAAPPPPPPPPPPP..PPPII........ GG....GGGGGGGGG.GGGEEEEEEEEEEE...EELLL..........LLAAA...AAAAA.......TTTT....TTTTT........OOOOO..
##.PPPPPPPPPPPP...PPAAAAAAAAAAAA..AAAPPPPPPPPPP...PPPII........ GGG...GGGGGGGGG.GGGEE............EELLL..........LLAAAAAAAAAAAA......TTTT....TTTTTT.......OOOOO..
##.PPPPP.........PPPAAAAAAAAAAAA..AAAPP...........PPPII......... GGG.......GGGGG.GGGEE............EELLL.........LLLAAAAAAAAAAAA......TTTT.....TTTTT.......OOOOO..
##.PPPPP.........PPPAAAAAAAAAAAA..AAAPP...........PPPII......... GGGG......GGGGG.GGGEE............EELLL.........LLLAAAAAAAAAAAA......TTTT.....TTTTTO.....OOOOOO..
##.PPPPP.........PPPAA.....AAAAAA.AAAPP...........PPPII......... GGGGGG.GGGGGGGG.GGGEE............EELLL.........LLLAA.....AAAAAA.....TTTT.....TTTTTOOO.OOOOOOO...
##.PPPPP........PPPPAA......AAAAA.AAAPP...........PPPII.......... GGGGGGGGGGGGGGG.GGGEEEEEEEEEEEE..EELLLLLLLLLLLLLLLAA......AAAAA.....TTTT......TTTTOOOOOOOOOOO...
##.PPPPP........PPPPA.......AAAAAAAAAPP...........PPPII...........GGGGGGGGGGGGGG..GGGEEEEEEEEEEEE..EELLLLLLLLLLLLLLLA.......AAAAAA....TTTT.......TTTOOOOOOOOOO....
##.PPPPP........PPPPA.......AAAAAAAAAPP...........PPPII.............GGGGGGGGGG....GGGEEEEEEEEEEEE..EELLLLLLLLLLLLLLLA.......AAAAAA....TTTT........TTOOOOOOOO......
##................................................................................................................................................................

import time
import math 
from typing import get_type_hints

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+             - Welkom bij Papi Gelato. -                   +")
print("+                 Waar ijs lekker is.                       +")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
time.sleep(2)

#Prijzen
Bollen = float(1.10)
Hoorentje = float(1.25)
Bakje = float(0.75)


#Toppingen
Geen = float(0.0)
Slagroom = float(0.50)
Sprinkels = float(0.30)
CaramelSaus = float(0.90)

#Doelgroepen
Particulier = "Particulier"
Zakelijk1 = "Zakelijk"

#Type ijs
A = "Bakje"
B = "Horrentje"

def zakelijk():
    print("Bent u paticulier of zakelijk?")
    Doelgroep = input()
    if Doelgroep == "Paticulier" or "paticulier" :
        Doelgroep = Particulier
    elif Doelgroep == "Zakelijk" or "zakelijk":
        Doelgroep = Zakelijk1
        print("U word verzonden naar een zakelijke aankoop...")
        time.sleep(2)
    else:
        print("U moet wel een juiste doelgroep kiezen..")
        return zakelijk()
zakelijk()
def stap1():
    print("Welke smaak wilt u? (Vanilla), (Chocolade), (Aardbij), (Mint)")
    Smaak = input()
    if Smaak == "Chocolade" or "Vanilla" or "Aardbij" or "Mint":
        print("Topping: (Geen) | (Slagroom) | (Sprinkles) | (CaramelSaus) ")
        Topping = input()
        if Topping == "Slagroom":
            Topping = Slagroom
        elif Topping == "Geen":
            Topping = Geen
        elif Topping == "Sprinkles":
            Topping = Sprinkels
        elif Topping == "CaramelSaus":
            Topping = CaramelSaus
        else:
            print("U moet wel iets kiezen")
            stap1()
        print("Hoeveel bolletjes wilt u?")
        Bolletjes = int(input())
        if Bolletjes <= 3:
            print('Wilt u ' + str(Bolletjes) + (' Bolletje: een hoorntje of een bakje?'))
            vraag = input()
            if vraag == "Hoorntje" or "Bakje":
                def menu():
                    print('------["Papi Geleto"]-------')
                    print('Doelgroep: ' + Zakelijk1 + Particulier)
                    print('Smaak: ' + Smaak)
                    print('Bolletjes: ' + str(Bolletjes) + ' =  €' + str(Bollen))
                    print('Topping: ' + str(Topping))
                    print('Op-eetkeus: ' + vraag)
                    print('----------------------------')
                    print('Te betalen:  €' + str(Bollen * Bolletjes + Topping))
                    time.sleep(5)
                    print("Nog anders iets bestellen?")
                    bestellen = input()
                    if bestellen == "Ja":
                        stap1()
                    elif bestellen == "Nee":
                        print("Bedankt en tot ziens")
                    else:
                        print("Sorry, dat snap ik niet...")
                        stap1()
                menu()
        elif Bolletjes <= 8:
            print("Dan krijgt u van mij een bakje met " + str(Bolletjes) + " bolletjes")
            time.sleep(2)
            print('------["Papi Geleto"]-------')
            print('Doelgroep: ' + Zakelijk1 + Particulier)
            print('Smaak: ' + Smaak)
            print('Bolletjes: ' + str(Bolletjes) + ' =  €' + str(Bollen))
            print('Topping: ' + str(Topping))
            print('Op-eetkeus: Bakje')
            print('----------------------------')
            print('Te betalen:  €' + str(Bollen * Bolletjes + Topping))
            time.sleep(5)
            print("Nog anders iets bestellen?")
            bestellen = input()
            if bestellen == "Ja":
                stap1()
            elif bestellen == "Nee":
                print("Bedankt en tot ziens")
            else:
                print("Sorry, dat snap ik niet...")
                stap1()
        else:
            print("Sorry ik begrijp het niet..")
            stap1()
    else:
        print("Zulke grote bakken hebben we niet.")
        return stap1()
stap1()