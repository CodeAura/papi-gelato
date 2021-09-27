import time
import math

def ijsbak():
    print("Helaas zulke grote bakken hebben we niet")

def ijsinput():
    print("Dat is helaas niet mogelijk")

def bolletjes():
    print("+++++++++++++++++++++++++++")
    print("+ Welkom bij Papi Gelato. +")
    print("___________________________")
    time.sleep(1)
    print(" je mag alle smaken kiezen zolang het maar vanille ijs is.")
    print("+++++++++++++++++++++++++++")
    time.sleep(2)
    print("Hoeveel bolletjes wilt u?")
    bol = int(input())
    if bol >= 1:
        print("Wilt u deze bolletje(s) in A) een hoorntje of B) een bakje?")
        AB = input()
        if AB == "A":
            print("Hier is uw {hoorntje/bakje} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N)")
            bestellen = input()
            if bestellen == "Y":
                bolletjes()
            else:
                print("Bedankt en tot ziens!")
        else:
            print("Helaas zijn de bakjes niet in vooraad.")       
    elif bol >= 4:
        print("Dan krijgt u van mij een bakje met bolletjes")
    elif bol >= 8:
        ijsbak()
    else:
        ijsinput()
