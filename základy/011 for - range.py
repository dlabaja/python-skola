# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 09:17:29 2011

@author: Radek
"""
"""
Cyklus for
----------
- jedná se o cyklus s řídící proměnnou
- dopředu je znám počet opakování
- nemůže nastat nekonečný cyklus

Princip
- řídící proměnná postupně nabývá všech hodnot z
  pevně dané množiny
- pro každou hodnotu se vykoná jedna iterace  

Pozn!
Fce range() pracuje pouze s celými čísly.
Lze použít i záporná čísla.


for i in [množina hodnot]:
    tělo cyklu
"""

# for i in 1,3,14,2,9,1000:
#     print (2*i)


# retezec="Olomouc"
# for i in retezec:
#     print (i)

 
# for i in range(15):     #[0,1,2,...,14]
#       print (i)

#pocatecni hodnota i=0
#krok=1
#koncova hodnota i=14


# for i in range(5,10):
#     print (i)
   
#pocatecni hodnota i=5
#krok=1
#koncova hodnota i=9

# for i in range(100,10,-5):  #[100,95,80,...15]
#     print (i)

#pocatecni hodnota i=100
#krok=-5
#koncova hodnota i=15

"""
Úkol:
1) Načtěte z klávesnice číslo x a vypište pod sebou x hvězdiček.
2) Vypište posloupnost čísel 52, 54, ..., 78.
3) Vypište náhodný počet (1-50) náhodných čísel (1-100).
4) Načtěte číslo a vypište všechny jeho celočíselné dělitele.
5) Zjistěte, zda zadané číslo je prvočíslo.
"""
import random

def hvezdicky():
  vstup = int(input("Zadejte číslo: "))
  for i in range(vstup):
    print("*")

def posloupnost():
  for i in range(52, 79, 2):
    print(i)

def nahodna_cisla():
  vstup = int(input("Zadejte počet náhodných čísel: "))
  for i in range(vstup):
    print(random.randint(1,100))

def delitele():
  vstup = int(input("Zadejte číslo: "))
  delitele = []
  for j in range(1, vstup + 1):
    if vstup % j == 0:
      print(f"Číslo je dělitelné {j}")
      delitele.append(j)

  if len(delitele) == 2:
    print("Číslo je prvočíslo")

delitele()










