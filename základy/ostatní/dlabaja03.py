#skupina A

"""
Načtěte z klávesnice horní číslo. Vypište sestupně pod sebe všechny hodnoty od zadaného čísla až po nulu. Použijte cyklus while.

Př:
Zadej horní číslo: 11

11
10
9
8
7
6
5
4
3
2
1
0

"""

def sestupna_cisla():
    i = int(input("Zadej horní číslo: "))
    while i >= 0:
        print(i)
        i -= 1

"""
Načtěte z klávesnice počet řetězců – tj. kolik se jich bude následně zadávat. Pak řetězce načítejte z klávesnice postupně pomocí cyklu a průběžně spojujte do jednoho. 
Na závěr vypište spojený řetězec.

Př:
Zadej počet řetězců: 4

Zadej řetezec: VOS
Zadej řetezec: a
Zadej řetezec: SPSE
Zadej řetezec: Olomouc

Výsledek: VOS a SPSE Olomouc
"""

def nacitani_retezcu():
    pocet = int(input("Zadejte počet řetězců: "))
    retezec = ""
    while pocet > 0:
        retezec += f"{input('Zadejte řetězec: ') } "
        pocet -= 1
    print(f"Výsledek: {retezec}")