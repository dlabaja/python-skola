# -*- coding: utf-8 -*-
"""
Created on Wed Feb 29 07:56:55 2012

@author: Martin
"""
"""
Výjimky
- slouží k zachycení chyb a problémových stavů
try:
    blok s kódem, kde může nastat chyba
except:
    blok, který se provede při chybě
else:
    nepovinný blok, který se provede, když nenastane
    chyba    
"""

# import math

# cislo=-10
# try:
#     odmocnina=math.sqrt(cislo)
#     print("Odmocnina z",cislo,"je",odmocnina)
# except:
#     print("Chyba, odmocnit lze jen nezáporná čísla!")    


# x=8
# y=0
# try:
#     print ("Pokus o výpočet podílu")
#     vysledek=x/y
#     print (vysledek)
# except:
#     print ("Nastala chyba deleni")
# else:    
#     print ("Deleni probehlo v poradku.")



# import math
# vstup=False
# while (vstup==False):
#     try:
#         cislo=float(input("Zadej cislo:"))
#         odmoc=math.sqrt(cislo)
#         print(odmoc)
#     except:
#         print("Zadávejte pouze kladná čísla!!!")
#     else:    
#         vstup=True


# try:
#     c=4+2
#     raise IndexError
#     input("Zadej číslo: ")
# except IOError:
#     print ("Chyba vstupu nebo vystupu")
# except ZeroDivisionError:
#     print ("Nastala chyba deleni nulou")
# except NameError:
#     print ("Chyba jmena ")
# except:
#     print ("Jina vyjimka")
# else:
#     print ("OK")

"""
Ukoly:
1) Ošetřete pomocí výjimky převod řetězce na číslo.
"""

def prevod():
    try:
        cislo = int("cislo")
    except:
        print("Tento řetězec nelze převést na číslo")

"""
2) Spusťte v části try nějakou funkci a dejte jí
   špatný počet parametrů. 
"""

def funkce():
    try:
        ord("toto není char")
    except:
        print("Měl být zadaný char, ne string > 1")

"""
3) Vytvořte si seznam o délce 3 a zkuste vypsat 
   4. prvek.
""" 

def seznam():
    print(["i", "d", "k"][4])









