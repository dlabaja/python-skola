# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:17:39 2012

@author: Radek
"""

"""
N-tice (tuple)
- vytvářejí se pomocí ()
- jsou neměnné, obdobně jako řetězce
- nemají žádné metody (jako např. pop(),...)
"""
#ntice=()
#print (ntice)


# x=(7,'Ahoj',4.7,None)
# print(x)
# print(x[1])

#a=b=c=1
#ntice=(a,b,c)
#print (ntice)

# pokus=1,2,3
# print(pokus)

"""n1=tuple("Ahoj")
n1=list(n1)
print (n1)"""


"""
Úkol:
1) Vytvořte n-tici s třemi náhodnými čísly a 
   vypište ji.   
2) Vygenerujte seznam s 10-ti tříprvkovými n-ticemi.
   Náhodná čísla budou z intervalu <0,1>.
   Nakonec seznam vypište tak, aby n-tice byly pod 
   sebou.
"""

import random

def nahodna_cisla():
   print((random.randint(0,10), random.randint(0,10), random.randint(0,10)))

def seznam():
   seznam = []
   for i in range(10):
      seznam.append((random.randint(0,1), random.randint(0,1), random.randint(0,1)))
      print(seznam[i])

seznam()





   