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
    odpovedi = ["No poklad?", "Umřel jsi", "Našel jsi poklad", "Prázdná místnost", "Zamknuté dveře", "Tam bych nešel, programuje tam děsivý Dan v děsivém pythonu", "Tady dveře nejsou", "Dveře zmizely :(("]
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
        elif odpoved == "Umřel jsi":
            exit()

hra()