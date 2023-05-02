# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 08:35:56 2011

@author: Radek
"""
"""
Podmíněný příkaz (if) - umožňuje rozhodování
--------------------------------------------
if PODMÍNKA1:
    odsazené příkazy (blok1)
elif PODMÍNKA2:    
    odsazené příkazy (blok2)
elif ...
    ...    
else:
    odsazené příkazy (blokN)

Pozn. 
Části elif a else jsou nepovinné.
"""

# x=float(input("Zadej cislo:"))
# if x>0: 
#     print ("Cislo je kladne!")
#     print ("Provedla se prvni vetev prikazu IF")
# elif x==0:
#     print ("Nula")
# else:
#     print ("Cislo je zaporne")


# print(15<8)
   
"""
Relační operátory
>  větší   >= větší nebo rovno
<  menší   <= menší nebo rovno
== rovno   != nerovno

in testuje přítomnost prvku v množině
"""

# Testování intervalu
# x = 20
# if 5 < x < 15:
#     print("Platí")
# else:    
#     print("Neplatí")


"""retezec="Python je programovací jazyk"
if "programy" in retezec:
    print("Ano, je tam.")
else:
    print("Ne, není tam.")



Úkol:
1) Načtěte z klávesnice 2 čísla a zjistěte, které z
   nich je větší, nebo jestli jsou stejná.
2) Načtěte celé číslo a zjistěte, zda je liché či sudé.
3) Načtěte řetězec (heslo) a zjistěte jestli je správné.
   Správné heslo je "klokan".
4) Načtěte koeficienty kvadratické rovnice, zjistěte
   kolik má řešení a vypište její řešení.  
   Testovací hodnoty:
   a = 1, b = -3, c = 2 -> x1 = 2, x2 = 1
   a = 1, b = -2, c = 1 -> x1 = 1
   a = 1, b = -2, c = 2 -> nemá řešení
"""   

def a():
    a = float(input("Zadejte číslo 1: "))
    b = float(input("Zadejte číslo 2: "))
    if a < b:
        print("Druhé je větší")
    elif a > b:
        print("První je větší je větší")
    else:
        print("Všechna jsou stejná")

def b():
    a = int(input("Zadejte číslo: "))
    if a % 2 == 0:
        print("Číslo je sudé")
        return
    print("Číslo je liché")

def c():
    if "klokan" == input("Zadejte heslo: "):
        print("Heslo je správné")
        return
    print("Heslo je špatné")

import math

def d():
    a = int(input("Zadejte číslo A: "))
    b = int(input("Zadejte číslo B: "))
    c = int(input("Zadejte číslo C: "))
    d = b * b - 4 * a * c
    if d >= 0:
        print(f"x1 = {(-b + math.sqrt(d))/(2*a)}, x2 = {(-b - math.sqrt(d))/(2*a)}") 
        return
    print("Rovnice nemá řešení")

"""
Textová hra Najdi poklad
Výpis:
Jsi v místnosti. Můžeš jít dál všemi 4-mi směry.
a) Jdi na sever
b) Jdi na jih
c) Jdi na západ
d) Jdi na východ
Zadej volbu:

Podle volby přejdeme do další místnosti, kde
nám hra nabídne další 3 směry.
Tam je pak buď poklad nebo něco jiného.
Poté program skončí.    

Texty použijte svoje např:
a) Tahle cesta nevede k pokladu.
b) Narazil jsi na strážce, který tě nepustil dál.
c) Našel jsi poklad!
d) Tato cesta vedla do prázdné místnosti.

    
Důležité:
Pokud uživatel zadá špatně vstup, program skončí a 
zobrazí se mu něco na tento způsob:
   
"Chyba vstupu, spusťte hru znovu!"    
"""

import random

def hra():
    odpovedi = ["No poklad?", "Umřel jsi lol", "Našel jsi poklad", "Prázdná místnost", "Zamknuté dveře", "Tam bych nešel", "Tady dveře nejsou", "Dveře zmizely :(("]
    vstup = ["S", "J", "Z", "V"]
    print("Vítejte ve hře, pohybujte se příkazy S (sever), J (jih), Z (západ), V (východ)")
    while True:
        if input("Zadejte směr: ") not in vstup:
            print("Neplatný směr, spusťe hru znovu")
            exit()
        odpoved = odpovedi[random.randint(0, len(odpovedi) - 1)]
        print(odpoved)
        if odpoved == "Našel jsi poklad":
            print("Vyhráli jste")
            exit()
        elif odpoved == "Umřel jsi lol":
            exit()

hra()
















