# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:24:01 2012

@author: Martin
"""
"""
Styly čar
ro  - červená kolečka
bs  - modré čtverečky
g^  - zelené trojúhelníky
y-  - žlutá plná čára
--  - čárkovaná čára
:   - tečkovaná
""" 

import pylab as p

x=[1,2,3,4]
y=[1,4,9,16]

p.plot(x,y,"g:s") #vložení bodů do grafu 'barvatvar'
# p.axis([0, 10, 0, 10]) #rozsah os x a y

# p.plot(x,y,'ro') #vložení bodů do grafu 'barvatvar'

# p.plot(x,y,color="green")
# p.plot(x,y,'g--',color="#ff0000") #vložení bodů do grafu 'barvatvar'


p.show()

"""
Úkol:
1) Vykreslete graf funkce y=x**3-2*x**2+x-1 jako 
   plnou čáru s kulatými vrcholy.
2) Vygenerujte seznam 20-ti náhod. bodů v rovině (0,20)
   a zobrazte jej pomocí čtverečků.   
3) Načtěte z klávesnice souřadnice tří bodů a zobrazte 
   trojúhelník. 
""" 






  
