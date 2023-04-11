 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:53:10 2012

@author: Martin
"""
import pylab as p

x=p.arange(1,2*p.pi,0.1)
y=p.sin(x)

p.fill(x,y,"#00ff42")
p.plot(x,y,linewidth=3)
p.grid(True)
p.show()