# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:49:39 2011

@author: Radek
"""
"""
Logické operátory dle priority
not - negace (unární)
and - logický součin (binární)
or  - logický součet (binární)

Priorita je stejná jako u aritmetických operací.
"""

# slovo=input("Zadej slovo: ")
# if not slovo=="Python":
#         print("Nezadal jsi Python!")

# if slovo!="Python":
#         print("Nezadal jsi Python!")


"""
rok = int(input("Zadej rok:"))
if rok>=2000 and rok<=2099:
    print ("Rok patří do 21. století")
else:
    print ("Rok nepatří do 21. století")

Úkol:
1) Načtěte strany trojuhelniku a zjistete, zda lze
   sestrojit.
2) Navic zjistete, jestli je pravouhly.
3) Načtěte souřadnice bodu (x,y) a rozhodněte, ve 
   kterém kvadrantu bod leží, či zda je na ose.
4) Načtěte rok a zjistěte, zda je přestupný. 
   (jsou to roky dělitelné 4, roky dělitelné 100 nejsou 
   přestupné, roky dělitelné 400 přestupné jsou)
""" 


def trojuhelnik():
   a = float(input("Zadejte stranu a: "))
   b = float(input("Zadejte stranu b: "))
   c = float(input("Zadejte stranu c: "))
   if a + b > c or b + c > a or a + c > b:
      print("Trojuhelnik lze narysovat")
      if c*c == a*a + b*b or a*a == c*c + b*b or b*b == a*a + c*c:
         print("Trojuhelnik je pravouhly")
      return
   print("Trojuhelnik nelze narysovat")

def souradnice():
   x = float(input("Zadejte x: "))
   y = float(input("Zadejte y: "))
   if x == 0 or y == 0:
      print("Bod leží na ose")
   elif x > 0 and y > 0:
      print("První kvadrant")
   elif x < 0 and y > 0:
      print("Druhý kvadrant")
   elif x < 0 and y < 0:
      print("Třetí kvadrant")
   elif x > 0 and y < 0:
      print("Čtvrtý kvadrant")

def rok():
   rok = int(input("Zadejte rok: "))
   if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
      print("Rok je přestupný")
      return
   print("Rok není přestupný")

rok()
   















