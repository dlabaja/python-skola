# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:44:08 2012

@author: Martin
"""
"""
text (x,y,řetězec) 
     - umístí řetězec na zvolené souřadnice v grafu
     - automaticky se vkládá nad y a vpravo od x, ale způsob
       zarovnání můžeme změnit pomocí nepovinných parametrů

annotate (řetězec,xy=(x,y),xytext=(x,y),arrowprops=dict(facecolor=color,shrink=x))
     - poznámka s šipkou
     - šipka ukazuje od poznámky na bod xy
     - poznámka je umístěna na souřadnicích xytext
     - vlastnosti šipky se definují v arrowprops, shrink znamená zkrácení
       šipky v obou směrech, uvádí se jako desetinné číslo (0.25 = čtvrtina)
"""

import pylab as p

# x=p.arange(-2,3,0.01)
# y1=x**2-1
# y2=2*x+1
# p.fill_between(x,y1,y2,where=(y2>y1), facecolor="gray")
# p.plot(x,y1,"black")
# p.plot(x,y2,"black")
# p.text(0,0,'Popisek',fontsize="14", color="blue")
#horizontalalignment='right',verticalalignment='center',color="r")

# p.annotate('Vybarvená plocha', xy=(1,2), xytext=(-1.5,5), 
#           arrowprops=dict(facecolor='red'))
# p.grid(True) 
# p.show()


"""
Úkol:
1) Nakreslete funkci y1=-(x-2)^2 + 4.
   Vykreslete přímku y2=x čárkovanou čarou.
   Vybarvěte plochu mezi oběma čarami tam, kde platí
   že (y1>y2).
   Doplňte šipku s popisem směřující přibližně na střed
   vybarvené plochy.
   Pojmenujte průsečíky čar písmeny A a B.
   Přidejte legendu s popisem obou čar.
"""   

def texty():
  x = p.arange(-0.5, 4, 0.1)
  y1=-(x-2)**2 + 4
  y2=x
  p.plot(x, y1, label="$y=-(x-2)^2+4$")
  p.plot(x, y2, label="$y=x$")
  p.fill_between(x,y1,y2,where=(y1>y2), facecolor="gray")
  p.annotate('Vybarvená plocha', xy=(1.7,2.8), xytext=(2,-1), arrowprops=dict(facecolor='red'))
  p.annotate('A', xy=(0.03,-0.2))
  p.annotate('B', xy=(2.95,2.6))
  p.legend(loc="best")
  p.show()

texty()
