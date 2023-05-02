# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 08:19:51 2011

@author: Radek
"""

"""
Opakování
1) Vytvořte si proměnné pro výšku a průměr sklenice tvaru válce.
   Proměnným nastavte vámi zvolené hodnoty v cm.
   Vypočítejte a vypište objem sklenice i s jednotkami.
2) Zadejte si u sklenice objem v ml a průměr.
   Dopočítejte a vypište výšku.
"""
v = 3
r = 2 / 2
objem = 3.14 * r * r * v
print(f"{objem} cm")

dalsiobjem = 1000
dalsir = 2 / 2
vyska = dalsiobjem / (3.14 * dalsir * dalsir)
print(f"{vyska}")


"""
Řetězce (string)
- jsou uzavřeny v uvozovkách nebo apostrofech
- délku zjistíme pomocí fce len()
- k jednotlivým znakům řetězce můžeme přistupovat
  pomocí indexu, první znak má index 0
- řetězce lze sčítat a násobit celým číslem
"""

# ret='VOS a "SPSE" Olomouc'
# print (ret)

ret="VOS a \"SPSE\" Olomouc"
# print (ret)

# delka = len(ret)
# print ("Delka je", delka)

# print (ret[2])


# ret2 = "je nejlepsi skola"
# vysledek = ret +" "+ ret2
# print (vysledek)

# vysledek=5*"Skola"
# print (vysledek)


# tab="<table border=\"1\">"
# tab=tab+10*"\n<tr><td>Buňka 1</td><td>Buňka 1</td>" 
# tab=tab+"\n</table>"
# print(tab)

"""
Úkol:
1) Vložte do proměnné nějaký text. Vypište 
   proměnnou. Vypište délku textu. Vypište
   prostřední písmeno textu.
2) Vypište 1000 uvozovek. Ověřte jejich délku
   pomocí funkce len().
"""

def text():
   text = "abcdefgh"
   print(f"{text} - délka je {len(text)}")

def uvozovky():
   uvozovky = 1000*'"'
   print(uvozovky)
   print(len(uvozovky))




























