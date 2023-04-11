# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:34:21 2012

@author: Martin
"""
"""
subplot(x,y,z) - specifikuje, do kterého grafu v aktuálním obrázku se
                 bude kreslit (x=pocet řádků, y=pocet sloupců, z=číslo
                 grafu)
               - rozložení x a y musí být stejné  
"""

import pylab as p

p.subplot(2,2,1)
p.plot([1,2,3,5], linewidth=4)
p.plot([3,1,5,2])
p.title("Graf 1")


p.subplot(2,2,2)
p.plot([3,2,6,2])
p.title("Graf 2")

p.subplot(2,2,3)
p.plot([1,2,3,5],"y--", linewidth=4)
p.plot([3,1,5,2])
p.title("Graf 3")

p.subplot(2,2,4)
p.plot([3,2,6,2])
p.title("Graf 4")

p.show()



"""
Úkol:
1) Zabrazte fci y=|x-1|+1 ve dvou grafech pod sebou, 
   pokaždé jinou barvou a jinou tloušťkou.
   Použijte funkci abs().
"""
