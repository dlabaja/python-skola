# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:59:50 2012

@author: Martin
"""
"""
Připojení knihovny
    1) import knihovna  -> knihovna.funkce()
    2) import knihovna as m -> m.funkce()
    3) from knihovna import * -> funkce() 
       - POZOR, může dojít k přepsání importovaných
       proměnných nebo fcí, pokud se v importovaných
       knihovnách jmenují stejně
"""

import math     #připojení knihovny math

# print ("Číslo pí: ", math.pi)
# print ("Eulerovo číslo: ", math.e)


# print ("Absolutní hodnota: ",abs(-67.5))
# print ("Odmocnina: ", math.sqrt(16))


# print ("Sinus 30°: ", math.sin(math.pi/180*30))
# print ("Cosinus 45°: ", math.cos(math.radians(45)))
# print ("Tangens 45°: ", math.tan(math.radians(45)))


# print ("Useknutí desetinné části: ", math.trunc(61.4788))
# print ("Zaokrouhlení nahoru: ", math.ceil(61.4788))
# print ("Zaokrouhlení dolů: ", math.floor(61.4788))
# print ("Zaokrouhlení: ", round(61.4788,2)) #není v math


# print ("Logaritmus: ", math.log(1024,2))

"""
Ukol:
1)Spočítejte odmocninu ze zlomku 8/3. 
"""    

def odmocnina():
  print(math.sqrt(8/3))

"""
2)Uživatel zadá 2 odvěsny v pravoúhlém trojúhelníku. 
  Spočítejte délku přepony.
  Výsledek zaokrouhlete na 1 des. místo.  
"""

def trojuhelnik():
  print(f"Přepona má délku {round(math.sqrt(math.pow(int(input('Zadejte stranu a: ')), 2) + math.pow(int(input('Zadejte stranu b: ')), 2)), 1)}")

""" 
3)Díváte se na strom ze vzdálenosti 100m pod 
  úhlem 20°. Jak je vysoký?
  Výsledek zaokrouhlete směrem dolů na celé metry.
  (Mělo by vyjít 36m)
"""

def strom():
  print(100*math.tan(20*(math.pi/180)))

"""
4)Upravte předchozí program tak, aby vzdálenost a 
  úhel mohl zadat uživatel z klávesnice.
"""

def strom2():
  print(int(input("Zadejte vzdálenost"))*math.tan(int("Zadejte úhel")*(math.pi/180)))





