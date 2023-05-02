# -*- coding: utf-8 -*-
"""
Formátovaný řetězec pomocí funkce format()
- do řetězce vkládáme pomocí indexů hodnoty
  z n-tice
- obecný tvar je:
  retězec="{index:specifikátor}".format(n-tice)

https://www.sallyx.org/sally/python/python3b.php#format3
https://docs.python.org/3/library/string.html#format-specification-mini-language
http://howto.py.cz/cap06.htm#17
"""
# d = 8
# m = 5
# r = 2022


# Méně vhodný způsob
# datum = str(d) + ". " + str(m) + ". "+ str(r)
# print(datum)

# hodnoty se dosadí do řetězce dle {indexů}
# ret = "Dnes je {0}. {1}. {2}".format(d,m,r)
# print(ret)

# indexy parametrů lze vynechat :)
# ret = "Dnes je {}.{}.{}".format(d,m,r)
# print(ret)

# hodnoty se dosadí do řetězce dle {indexů}
# ret = "Dnes je {0:2}. {1:02}. {2}".format(d,m,r)
# print(ret)


# vložení desetinného čísla (dochází k matemat. zaokr.)
# ret = "Číslo pí má hodnotu {0:8.3f}".format(3.14159)
# print(ret)

# lze vkládat i hodnoty z různých struktur
# seznam=["Chleba","stojí",28.50,"Kč"]
# ret="{0[0]} {0[1]} {0[2]:10.2f} {0[3]}".format(seznam)
# print(ret)

# pozor, u slovníků se nepíší uvozovky u klíče!!!

# lze uvádět různé soustavy celého čísla
# (b = binárně, x = hexadecimálně, c = znak)
# ret = "Číslo {0} je binárně {0:b}".format(2022)
# print(ret)
# ret = "Číslo {0} je hexadecimálně {0:x}".format(2022)
# print(ret)
# ret = "Znak s kódem {0} je znak {0:c}".format(64)
# print(ret)

# v rámci volného prostoru můžeme obsah zarovnávat nebo i
# vyplnit nějakým znakem, automaticky se vyplňuje mezerami

# ret="Číslo {:<15} zarovnané doleva".format(28)
# print(ret)
# ret="Číslo {:0>15} zarovnané doprava".format(28)
# print(ret)
# ret="Číslo {:^15} zarovnané na střed".format(28)
# print(ret)
# ret="Číslo {:*^15} zarovnané na střed".format(28)
# print(ret)

from datetime import datetime, timedelta
import random

"""
Úkol:
1) Vypište pod sebou 10 náhodných časových údajů ve 
   formátu hh.mm.ss.
"""

def casove_udaje():
    for _ in range(10):
        date = datetime.now() + timedelta(seconds=random.randint(0, 1000),
                        minutes=random.randint(0, 1000), hours=random.randint(0, 1000))
        print(f"{date.hour:02d}.{date.minute:02d}.{date.second:02d}")

"""
2) Vložte číslo 20 4krát do řetězce. Desítkově, binárně, 
   hexadecimálně a jako znak. 
"""

def dvacitka():
   print(f"{20}, {20:b}, {20:x}, {20:c}")

"""
3) Vypište pod sebe 10 náhodných čísel z 
   intervalu (0-1000) na 5 míst s měnou 'Kč' tak, aby:
   a) čísla ve sloupci byla zarovnána vlevo
      12   Kc
      897  Kc
      6    Kc
   b) čísla ve sloupci byla zarovnána vpravo     
        12 Kc
       897 Kc
         6 Kc
"""

def sloupec():
   for _ in range(10):
      print(f"{random.randint(0, 1000):<5}Kč") # doleva
      # print(f"{random.randint(0, 1000):>5}Kč") -> doprava
