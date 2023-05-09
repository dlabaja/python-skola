# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:01:45 2012

@author: Martin
"""
"""

Převody znaků
ord() - převede znak na jeho ordinální hodnotu (číslo)
chr() - opačná funkce, získáme znak = jednoznakový řetězec
"""


# znak=input('Zadej znak: ')
# cislo=ord(znak)
# print(cislo)


# cislo=int(input('Zadej cislo znaku: '))
# znak=chr(cislo)
# print (znak)


"""
Ukol:
1) Vypište úsek ASCII tabulky od 50 do 100
"""

import random
def ascii():
    for i in range(50, 101):
        print(chr(i))

"""
2) Vypište abecedu z malých písmen do řádku.  
"""

def mala_pismena():
    for i in range(ord('a'), ord('z')):
        print(chr(i), end='')

"""
3) Vygenerujte a vypište náhodné Velké písmeno.
"""

def nahodne_pismeno():
    print(chr(random.randint(ord('A'), ord('Z'))))

"""
4) Načtěte slovo a vypište jeho znaky posunuté o 1.
"""

def caesar():
    input = input("Zadejte slovo")
    for i in range(len(input)):
        print(chr(ord(input[i]) + 1), end='')

"""
5) Napište funkci, která vygeneruje náhodný řetězec z 
   libovolných malých písmen. Délka bude náhodná 
   mezi 10 a 1.
"""

def retezec():
   str = ""
   delka = random.randint(1, 10)
   for _ in range(len(delka)):
      str += chr(random.randint(ord('A'), ord('Z')))
   return str

"""
*) Rozšiřte předchozí funkci tak, aby se střídaly 
   souhlásky a samohlásky. Slovo začíná náhodně 
   samohláskou nebo souhláskou.
"""

def retezec2():
   str = ""
   delka = random.randint(1, 10)
   samohlasky = "aeiouy"
   souhlasky = "bcdfghjklmnpqrstvwxz"
   j = random.randint(0,1)
   for i in range(delka):
      if (i + j) % 2 == 0:
         str += souhlasky[random.randint(0, len(souhlasky) - 1)]
         continue
      str += samohlasky[random.randint(0, len(samohlasky) - 1)]
   return str