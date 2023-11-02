# skupina A

import pylab as p

"""
Lomená čára a goniometrické funkce
Načtěte z klávesnice 2 seznamy. Seznam x-vých a seznam y-vých hodnot. Bude se jednat o 4 body v rovině.
Zobrazte 2 grafy v jednom obrázku tak, aby byly pod sebou.
První graf: 
•	Vykreslete lomenou čáru procházející zadanými body v seznamech.
•	Čára bude zelená, silná 2 pixely a body, kterými prochází, budou vykresleny jako červená kolečka. 
Druhý graf:
•	Zobrazte plochu mezi funkcemi y1=sin(2x) a y2=2cos(x) na intervalu <-2π, 2π>
•	Barvy funkcí (čar) zvolte modré, vyplněná plocha ať je žlutá
"""

def graf():
    x1 = []
    y1 = []
    for i in range(4):
        x1.append(int(input(f"Zadejte souřadnici x pro bod #{i+1}: ")))
        y1.append(int(input(f"Zadejte souřadnici y pro bod #{i+1}: ")))

    _, axs = p.subplots(2)
    axs[0].plot(x1, y1, marker = "o", ms = 5, mec = "r", mfc = "r", color="g", linewidth=2)

    x2 = p.arange(-2*p.pi, 2*p.pi, 0.1)
    ysin = p.sin(2*x2)
    ycos = p.cos(2*x2)

    axs[1].plot(x2, ysin, "b-", linewidth=1)
    axs[1].plot(x2, ycos, "b-", linewidth=1)
    axs[1].fill_between(x2,ysin,ycos,facecolor="#FFEA00")

    p.show()

"""
Napište funkci NahodnyCas(), která bude vracet náhodný časový údaj.
Časový údaj bude mít formát hh:mm:ss:ccc, kde:
•	hh jsou hodiny v intervalu 00 až 23
•	mm jsou minuty v intervalu 00 až 59
•	ss jsou sekundy v intervalu 00 až 59
•	ccc jsou milisekundy v intervalu 000 až 999
Údaj vytvořte jako řetězec pomocí funkce format() nebo pomocí fstringu.

Funkci vyzkoušejte použít v příkazu print(NahodnyCas()).

Př: 
Náhodný časový údaj:
12:34:25.871

Funkce – Krychle
Napište funkci Krychle(a), která vrací povrch krychle. Tato funkce bude mít jeden parametr – délku strany krychle. Pokud bude strana záporná, bude funkce vracet hodnotu 0. Povrch krychle spočítáme dle vzorce P=6aa.

Ukázka použití:
print(Krychle(2))
print(Krychle(-5))

Výstup:
24
0
"""

import random

def nahodnyCas():
    h = random.randint(0,23)
    m = random.randint(0,59)
    s = random.randint(0,59)
    c = random.randint(0,999)
    return f"{h:02d}:{m:02d}:{s:02d}:{c:03d}"

def krychle(a):
    if a < 0: return 0
    return 6*a*a
