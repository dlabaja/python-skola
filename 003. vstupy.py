def datum():
    den = 4
    mesic = 10
    rok = 2022
    datum = f"{den}.{mesic}.{rok}\n"
    print(datum)
    print(10*datum)

"""
Úkol:
1) Načtěte z klávesnice číslo a
   vypište zbytek po dělení číslem 10.
2) Načtěte z kláv. délku materiálu a na jak dlouhé
   kusy má být nařezán. Zjistěte kolik kusů získáte
   a jaký bude odpad.
3) Načtěte z kláv. ujeté kilometry (počet),
   spotřebované palivo (litry) a cenu za jeden litr.
   Spočítejte náklady na cestu, spotřebu na 100 km
   a náklady na 1 km. 

   Př: Vstup:  80 km, 4 l, 30 kč
       Výstup: 120 kč, 5.0 l, 1.5 kč
"""
def cislo():
    cislo = int(input("Zadejte číslo: "))
    print(cislo%10)

def delka():
    delka = int(input("Zadejte délku materiálu: "))
    kusy = int(input("Zadejte délku kusů k nařezání: "))
    print(f"Získáte {delka//kusy} kusů, zbyde vám {delka%kusy} m")

def kilometry():
    km = int(input("Zadejte délku počet ujetých km: "))
    palivo = int(input("Zadejte spotřebované palivo: "))
    cena = int(input("Zadejte cenu za litr: "))
    print(f"Palivo stojí {palivo*cena} Kč\nSpotřeba na 100 km je {(100*palivo)/km} l\nCena za 1km je {(palivo*cena)/km} Kč")

kilometry()