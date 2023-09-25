# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:54:17 2011

@author: Radek
"""
"""
Cyklus while
- umožňuje opakované provádění příkazů

while PODMÍNKA:
    odsazené příkazy (blok)

Princip:
- dokud platí podmínka, bude se provádět blok
- podmínka má stejnou podobu jako u IFu
- POZOR, může nastat nekonečný cyklus!    

Možnosti přerušení nekonečného cyklu:
1) Kliknout do výstupního okna a stisknout Ctrl+c
2) Zavřít Spyder
"""

# jmeno=input("Zadej jmeno: ")

# i=1
# while i<=10:
#     print(jmeno)
#     i+=1                #přičte hodnotu k proměnné i

# print (i)



#odhadněte, co bude dělat následující cyklus
#kdy skončí
#kolikrát proběhne

# import random
# x=1
# while x!=10:
#     x=random.randint(2,10)
#     print (x)


"""
Úkol:
1) Načítejte z klávesnice heslo, dokud nebude správně 
   zadáno. Správné heslo je "monitor".
2) Rozšíření úkolu 1). Zjistěte, na kolikátý pokus
   bylo heslo správně zadáno. 
3) Načtěte číslo n a sečtěte hodnoty od 1 do n
4) Vypište tabulku goniometrických funkcí pro úhly
   0 - 90° po 5-ti stupních. Pozor na nedefinované
   hodnoty. Čísla zaokrouhlete na 2 des. místa.
Výstup:
uhel sin	cos	   tg	 cotg
0° 	 0.0 	1.0    0.0 	 Inf.
5° 	 0.09 	1.0    0.09  11.43
...
90°	 1.0 	0.0    Inf.  0.0
   
""" 
"""
Navíc:
Načtěte od uživatele číslo a převeďte jej do
binární soustavy.    
"""

import math

def c():
   i = 0
   print("uhel\tsin\tcos\ttan\tcotg")
   while i <= 90:
      deg = (math.pi/180)*i
      sin = round(math.sin(deg), 2)
      cos = round(math.cos(deg),2)

      try:
         tan = round(math.tan(deg), 2)
      except:
         tan = "0"

      try:
         cotg = round(1 / tan, 2)
      except:
         cotg = "Inf"
      
      print(f"{i}\t{sin}\t{cos}\t{tan}\t{cotg}")
      i += 5 

def a():
   i = 0
   while input("Zadejte heslo: ") != "monitor":
      print("Zkuste to znovu")
      i += 1
   print(f"Heslo je správné, počet pokusů: {i}")

def b():
   vstup = int(input("Zadejte číslo: "))
   i = 0
   x = 0
   while i <= vstup:
      x += i
      i += 1
   print(x)

#opravit
def bin():
   cislo = int(input("Zadejte číslo: "))
   i = cislo
   bin = ""
   while i != 0:
      i = i//2
      print(i)
      if i == 1:
         bin += "0"
         continue
      bin += "1" 
   print(bin)
   
bin()




   





