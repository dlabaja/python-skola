# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:54:17 2011

@author: Radek
"""
"""
continue - přeruší aktuální iteraci, cyklus 
           pokračuje další iterací
break - přeruší vykonávání cyklu
"""           

"""
while True:
    heslo=input("Zadej vánoční kód:")
    if heslo=="jedle":
        break
    print("Špatný kód, zadej znovu.")

print("Spávný kód! Veselé Vánoce!")
"""


#co bude dělat tento cyklus a kdy skončí?

import random
x=1
while x!=10:
    x=random.randint(2,10)
    if x%2==0:
        continue
    print (x)
    if x==5:
        break



""" 
Úkol:
1) Pomocí cyklu načítejte 5 čísel z klávesnice. Když bude 
   zadáno záporné číslo, použijte break. 
2) Načtěte číslo a spočítejte je ciferný součet.
3) Naprogramujte hru myslím si číslo.
   Rozšíření: Vypsat počet pokusů.
"""













