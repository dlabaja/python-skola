# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:23:59 2012

@author: Martin
"""

"""          MODULY (knihovny)
Použití:
    1) import modul  -> modul.funkce()
    2) import modul as m -> m.funkce()
    3) from modul import * -> funkce() 
       - POZOR, může dojít k přepsání importovaných
       proměnných nebo fcí, pokud se v importovaných
       modulech jmenují stejně

Vlastní moduly:
    = obyčejné soubory s příponou *.py
    - při spuštění vznikne soubor *.pyc
    - z modulu můžeme použít globální proměnné a
    funkce
"""
"""
import mujsoubor.py
- příkazy -> provedou
- proměnné -> můžu je použít
- funkce (podprogramy) -> můžu je volat (spouštět)
"""

PI = 3.141

def PovrchKoule(r):
    return (4*PI*r**2)

"""
Úkoly:
    Vytvořte modul Telesa, ve kterém budou k
    dispozici tyto funkce pro výpočet objemů a povrchů:
    1) ObjemKrychle(a)
    2) PovrchKrychle(a)
    3) ObjemKvadru(a,b,c)
    4) PovrchKvadru(a,b,c)


    5) ObjemJehlanu (a,v)
    6) PovrchJehlanu (a,v)
"""    







