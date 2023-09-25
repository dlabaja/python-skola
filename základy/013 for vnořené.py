3# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:36:08 2013

@author: Radek
"""

"""
Vnořené cykly
"""


# sirka=int(input("Zadej šířku obdélníku:"))
# vyska=int(input("Zadej výšku obdélníku:"))

# for y in range(vyska):
#     for x in range(sirka):
#         print("* ",end="")
#     print() 

#Napsat kód pro čtverec.

      
"""
Úkol:
1) Vytvořte cyklus, který vypíše 6x dnešní datum.
   Celý cyklus zopakujte druhým cyklem 8x. 
"""

import datetime

def datum():
   for _ in range(8):
      for _ in range(6):
         print(datetime.datetime.now().date())

"""
2) Napište program, který 5x pod sebou vytiskne vaše 
   jméno (cyklem).
   Celý program zopakujte 30x (cyklem), vždy po 5-ti jménech
   vložte prázdný řádek.
   Napište před každé jméno jeho celkové pořadové číslo.
"""

def jmeno():
   for i in range(30):
      for j in range(5):
         print(f"{i*5+j} Jan Dlabaja") #i * range j + j
      print()

"""    
3) Vytvořte následující výpis pro libovolné n (toto bylo 4):
   1 : 1
   2 : 12 
   3 : 123
   4 : 1234
"""

def vypis():
   n = int(input("Zadejte číslo: "))
   strom = ""
   for i in range(1, n + 1):
      strom += str(i)
      print(f"{i} : {strom}")

"""
4) Načtěte n, vygenerujte n náhodných čísel a vypište
   ke každému z nich všechny jeho dělitele.
   Př: n=3
   4: 1 2 4
   18: 1 2 3 6 9 18
   11: 1 11
"""

import random

def rand():
   n = int(input("Zadejte počet náhodných čísel: "))
   for _ in range(n):
      cislo = random.randint(1, 100)
      delitele = []
      for j in range(1, cislo + 1):
         if cislo % j == 0:
            delitele.append(j)
      print(f"{cislo}: {delitele}")

"""
5) Vypište pyramidu z hvězdiček o výšce n.
   Př: n=4
      *  0*2+1 *; (3*2+1 - 0*2+1) / 2 = mezery na jedné straně
     ***  1*2+1
    *****  2*2+1
   *******  3*2+1
   Vytiskněte pod sebe několik náhodně velkých pyramid. Počet
   si zadá uživatel z klávesnice.
"""

def pyramida():
   n = int(input("Zadejte počet pater pyramidy: "))
   maxlen = (n-1)*2+1
   for i in range(n): #patra
      hvezdicky = i*2+1
      spaces = (maxlen - hvezdicky) // 2
      print(spaces * " " + hvezdicky * "*" + spaces * " ")
      
"""
6) Zkuste vytisknout šachovnici 8x8 (nxn) ze dvou zvolených znaků:
   . @ . @ . @ . @ x % 2 == 0 => . liché, @ sudé
   @ . @ . @ . @ . x % 2 == 1 => . sudé,  @ liché
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @ . @ .
"""

def sachenzie():
   for x in range(8):
      if x % 2 == 0:
         print(4*". @ ")
         continue
      print(4*"@ . ")

def sachenzie_but_better():
   n = int(input("Zadejte velikost šachovnice: "))
   for x in range(n):
      for y in range(n):
         print(f"{'.@'[y % 2 - x % 2]} ")
      print()

"""
7) Máme řetězec "abcdefghijklmnopqrstuvwxyz". Načtěte z
   klávesnice počet hesel a vygenerujte z počátečního
   řetězce daný počet náhodných hesel délky 7 znaků.
"""

def hesla():
   pocet = int(input("Zadejte počet hesel k vygenerování: "))
   abeceda = "abcdefghijklmnopqrstuvwxyz"
   hesla = []
   for _ in range(pocet):
      heslo = ""
      for _ in range(7):
         heslo += abeceda[random.randint(0, len(abeceda) - 1)]
      hesla.append(heslo)
   print(hesla)

sachenzie_but_better()








