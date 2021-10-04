import time

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+             - Welkom bij Papi Gelato. -                   +")
print("+ je mag alle smaken kiezen zolang het maar vanille ijs is. +")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
time.sleep(4)

def function():
    time.sleep(1)
    print("Hoeveel ijs bolletjes wilt u?")
    bol = int(input())
    if bol <= 1:
        def smaak():
            print("Welke smaak wilt u voor ijs bolletje nummer:  A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")
            Keuzeuit = input()
            if Keuzeuit == "V":
                print("U heeft voor vannilla gekozen")
                time.sleep(5)
                print("------------------")
                print(" + Papi Gelato +  ")
                print("------------------")
                time.sleep(1)
                print("Uw keuze:")
                print("------------------")
                print("Smaak:" + Keuzeuit)
                print("Aantal Bolletjes:" + bol)
                print("------------------")
            elif Keuzeuit == "C":
                print("U heeft voor chocolade gekozen.")
                time.sleep(5)
                print("------------------")
                print(" + Papi Gelato +  ")
                print("------------------")
                time.sleep(1)
                print("Uw keuze:")
                print("------------------")
                print("Smaak:" + Keuzeuit)
                print("Aantal Bolletjes:" + bol)
                print("------------------")
                print("Hoe wilt u betalen?")
                print("Ideal" "Paypal" "Mastercard" "Contant"
                input()
            elif Keuzeuit == "A":
                print("U heeft voor Aardbijen gekozen.")
                time.sleep(5) 
                print("------------------")
                print(" + Papi Gelato +  ")
                print("------------------")
                time.sleep(1)
                print("Uw keuze:")
                print("------------------")
                print("Smaak:" + Keuzeuit)
                print("Aantal Bolletjes:" + bol)
                print("------------------")
            elif Keuzeuit == "M":
                print("U heeft voor Munt gekozen.")
                time.sleep(5)
                print("------------------")
                print(" + Papi Gelato +  ")
                print("------------------")
                time.sleep(1)
                print("Uw keuze:")
                print("------------------")
                print("Smaak:" + Keuzeuit)
                print("Aantal Bolletjes:" + bol)
                print("------------------")
            else:
                print("U moet wel iets kiezen")
                time.sleep(1)
                opnieuw = input("Wilt u opnieuw proberen? ")
                if opnieuw == "Ja":
                    smaak()
                else:
                    print("Tot ziens!")     
        smaak()
    elif bol <= 4:
        print("Dan krijgt u van mij een bakje met ijs bolletjes")
        return 
    elif bol <= 8:
        print("Sorry, zulke grote bakken hebben we niet")
        menu = input("Terug naar het menu? (Y/N)")
        if menu == "Y":
            function()
        else:
            function()
    else:
        print("U moet wel iets kiezen")
        time.sleep(1)
        print("Opnieuw proberen?")
        Keuze2 = input()
        if Keuze2 == "Ja":
            function()
        else:
            print("Tot ziens!")
        
function()