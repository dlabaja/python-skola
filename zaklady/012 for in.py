# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 08:32:40 2011

@author: Radek
"""


#Lepší způsob
# for i in "Olomouc":
#     print(i)


#Horší způsob
# print()

# ret="Olomouc"
# for i in range(len(ret)):
#     print (ret[i])


"""
Úkol:
1) Načtěte řetězec z klávesnice. Vytvořte z něj nový 
   řetězec tak, že za každé písmeno vložíte znak "*". 
   "Python" -> "P*y*t*h*o*n*"
2) Načtěte řetězec a spočítejte v něm písmena "a".  
3) Načtěte řetězec a spočítejte součet všech cifer, 
   které se v něm budou vyskytovat.
"""

def retezec():
   vstup = input("Zadejte slovo: ")
   retezec = ""
   for i in vstup:
      retezec += f"{i}*"
   print(retezec)

def pocetpismen():
   vstup = input("Zadejte slovo: ")
   i = 0
   for item in vstup:
      if item == "a":
         i += 1
   print(f"Počet a: {i}")

def pocetpismenregex():
   vstup = input("Zadejte slovo: ")
   print(f"{len(list(filter(lambda item: item == 'a', vstup)))}")

def soucetcifer():
   vstup = input("Zadejte slovo: ")
   cifry = "1234567890"
   vysledek = 0
   for item in vstup:
      if item in cifry:
         vysledek += int(item)
   print(f"Výsledek je {vysledek}")

pocetpismenregex()




    
    
    
    