# -*- coding: utf-8 -*-
"""
Řetězce (string)
- uzavřeny v apostrofech (') nebo v uvozovkách (")
- trojí uvozovky mohou uzavírat i více řádků

Existuje i knihovna string
- obsahuje mnoho užitečných proměnných a funkcí

Např:
    string.ascii_letters
    string.digits
    atd.
"""

# x="""Víceřádkový
# pokusný
# řetězec
# """
# print(x)

"""
Speciální znaky - začínají lomítkem
\' - apostrof
\" - uvozovka
\\ - lomítko
\n - nový řádek
"""

# ret= "Specialni \nznaky: \' \\n \" "
# print(ret)

"""
Indexování
K jednotlivým částem řetezce lze přistoupit 
pomocí [].
Kladné hodnoty číslují znaky zleva, záporné zprava.      
"""

# ret="patek"
# print (ret[-1])

"""
Operátor : (slice)
- vrací podřetězec
[:n] - vrátí prvních n znaků
[n:] - vrátí podřetězec od pozice n do konce
[m:n] - vrátí podřetězec od pozice m do n
"""

# ret="abeceda"
# print (ret[:3])
# print (ret[-5:])
# print (ret[1:4])

"""
Funkce str()
- převede libovolný typ na řetězec
"""
# sez=[1,3,8]
# ret=str(sez)
# print (ret)
# print (sez[0])
# print (ret[0])

"""
Některé další řetězcové funkce
ret.split(znak,n) - vrátí seznam podřetězců, oddělovačem
                  je daný znak, automaticky je to mezera
                  - n říká, kolik odělovačů se použije
ret.replace("s1","s2") - nahradí v řetězci všechny 
                  výskyty s1 retezcem s2  

ret.upper() - vrátí řetězec převedený na velké znaky
ret.lower() - na malé znaky
"""

# veta="Toto je pokusná věta složená ze slov."
# seznam=veta.split(" ",3)
# print(veta)
# print(seznam)

# Převod řetězce na jednotlivá čísla + vložení do seznamu
# ret="22 3 28 20 16"
# sez=ret.split(" ")
# cisla=[]
# for i in sez:
#     cisla.append(int(i))
# print(sez)
# print(cisla)


# ret="Mival bil v Kijove"
# novy=ret.replace("i","y")
# print (novy)


# kod="<html> <H1>Nadpis</H1> </html>"
# novy=kod.replace("H1", "h1")
# print(novy)


"""
Úkol:
1) Načtěte z klávesnice řetězec, zjistěte jeho 
   délku a vypište:
   a) jeho prvních 5 znaků   
   b) jeho posledních 5 znaků
   c) jeho prostřední znak
"""

def nacitani_retezce():
    s = input("Zadejte řetězec: ")
    print(f"""Prvních 5 znaků: {s[0:5]}
Posledních 5 znaků: {s[len(s) - 5: len(s)]}
Prostřední znak: {s[len(s) // 2]}""")

"""
2) Načtěte řetězec čísel oddělených čárkami a 
   spočítejte součet těchto čísel.
   Př: vstup: 2,6,15,7
       vystup: 30
"""

def carky():
    soucet = 0
    for i in input("Zadejte řetězec: ").split(","):
        soucet += int(i)
    print(soucet)

"""
DU: Načtěte datum jako řetězec (dd.mm.rrrr) a vypište 
    jaké datum bude za 14 dnů opět v podobě řetězce. 
    Použijte split() pro získání částí data. #Není potřeba
"""

from datetime import datetime, timedelta

def datum():
    s = input("Zadejte datum: ")
    datum = datetime.strptime(s, '%d.%m.%Y') + timedelta(days=14)
    print(datetime.strftime(datum, '%d.%m.%Y'))

