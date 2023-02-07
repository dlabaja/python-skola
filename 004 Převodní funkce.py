# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:13:25 2012

@author: Martin
"""

"""
Převodní funkce
float() - převede hodnotu na desetinné číslo
10 -> 10.0
"10.154" -> 10.154

int() - převede hodnotu na celé číslo
      - desetinná část je odstraněna 
10.478 -> 10
"12" -> 12
"3.141" -> error!

str() - převede cokoli na  řetězec
400 -> "400"
10.478 -> "10.478"
(10+5j) -> "(10+5j)"

complex() - převede číslo na komplexní
"""


# x=input("Zadej číslo: ")
# x=float(x)
# print("Dvojnásobek:",2*x)


# y=float(input("Zadej desetinné číslo: "))
# y=int(y)
# print("Převedeno na celé:",y)


# x=1000
# text="Vysledek je "+str(x)+"."
# print(text)


"""
Úkol:
1) Načtěte z klávesnice desetinné číslo, 
   vydělte ho 3, převeďte zpět na řetězec 
   a přičtěte k němu jednotku "cm".
   Výsledný řetězec vytiskněte.

2) Načtěte rozměry domu s obdélníkovým 
   půdorysem jako celá čísla a spočítejte, 
   kolik m ctverečních polystyrenu potřebujete 
   na zateplení stěn (bez stropu a podlahy).   
"""

def descislo():
   print(f"{int(input('Zadejte desetinné číslo: ')) / 3} cm")

def dum():
   a = int(input("Zadejte šírku domu: "))
   b = int(input("Zadejte délku domu: "))
   c = int(input("Zadejte výšku domu: "))
   print(f"{2*c*(a+b)} m")



















