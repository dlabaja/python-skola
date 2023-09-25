# -*- coding: utf-8 -*-
"""
Generování náhodných čísel
---------------------------
V programech často potřebujeme získat náhodné číslo:
- počítač má vybrat z několika rovnocenných možností
  (třeba náhodné testové otázky, tahy hráče, házení
   kostkou, zamíchání karet)

Potřebujeme knihovnu random 
randint(od,do) - vygeneruje náhodné číslo z intervalu <od,do>
               - od a do musí být celá čísla, mohou být i záporná 
choice(data)   - vybere z dat náhodný prvek
               - data jsou obvykle řetězec nebo seznam
"""


import random


# x=random.randint(1,6)
# print ("Kostka hodila", x)

# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# print(pismeno)


# kod=""
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# print(kod)


"""mesic = random.randint(1,12)
print(mesic)
if mesic == (1,3,5,7,8,10,12):
    print("Plati")
else:    
    print("Neplati")
"""

"""
Úkol:
1) Naprogramujte hru KÁMEN, NŮŽKY, PAPÍR.
   Hraje člověk proti počítači.

Můžete vytvořit pomocné proměnné:
kamen=1
nuzky=2
papir=3

Náhled programu:
Hrajeme hru kámen, nůžky, papír
1) Kámen
2) Nůžky
3) Papír
Zadej svou volbu:
    
vyhodnocení + výpis + ošetření správného vstupu
"""


def kamennuzky():
    slovnik = {1: "kámen", 2: "nůžky", 3: "papír"}
    hrac = int(input("""Hrajeme hru kámen, nůžky, papír
1) Kámen
2) Nůžky
3) Papír
Zadej svou volbu: """))
    if hrac > 0 and hrac < 3:
        bot = random.randint(1,3)
        print(f"Bot hodil {slovnik[bot]}")
        if hrac == bot:
            print("Remíza")
        elif (hrac == 1 and bot == 2) or (hrac == 2 and bot == 3) or (hrac == 3 and bot == 1):
            print("Vyhráli jste")
        else:
            print("Prohráli jste")
        return
    print("Neplatné číslo")

kamennuzky()
