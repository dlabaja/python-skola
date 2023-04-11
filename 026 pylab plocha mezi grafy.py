# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:17:28 2012

@author: Martin
"""
"""
fill_between(x,y1,y2) - vyplní plochu mezi dvěma čarami, druhá je
                        nepovinná
                      - lze doplnit o podmínku   
facecolor="color"     - určuje barvu výplně 
"""

import pylab as p

x=p.arange(0,2*p.pi,0.1)
y1=p.cos(x)
y2=p.sin(x)
#y2=x/3


# p.plot(x,y1)
# p.plot(x,y2)
# p.fill_between(x,y1,y2,facecolor="yellow")


# p.plot(x,y1)
# p.plot(x,y2)
# p.fill_between(x,y1,y2,where=(y2<=0),facecolor="b")

p.plot(x,y1)
p.plot(x,y2)
p.fill_between(x,y1,y2,where=(y2>=0)*(x<=1),facecolor="g")

p.grid()
p.show()

"""
Úkol:
1) Vyplňte plochu mezi fcemi cos(x) a sin(2*x) fialovou 
   barvou v hexadecimálním tvaru na intervalu <0,2*pi>.
"""   