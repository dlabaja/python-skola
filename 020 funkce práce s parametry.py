# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 07:40:31 2012

@author: Radek
"""

# Defaultní parametry (předdefinované, implicitní)
def Vypis(x,y=5,z=6):
    print (x)
    print (y)
    print (z)

#Vypis(7,100,200)
# Vypis(z=100,x=200)


# Nepovinné parametry
def Vypis2(x,*parametry):
    print (x)
    print (parametry)


# Vypis2(100,"a","b","c","další hodnota")
# Vypis2(100)



# Kombinace všech možných druhů parametrů
# Nejprve se uvádí poziční parametry (positional, nondefault)
# Pak následují předdefinované (implictní, default)
# Nakonec jsou nepovinné parametry
def PokusSParametry(x,y=1,*z):
    print (x)
    print (y)
    print (z)

#PokusSParametry(10, 20, 1, 2, 3)

"""
Úkol:
1) Napište funkci Tisk, která bude mít proměnlivý 
   počet parametrů. Všechny parametry vytiskne pod
   sebe.
"""

def tisk(*parametry):
    print(parametry)

"""
2) Napište fci Soucet, která bude mít tři implicitní
   (defaultní) parametry nastavené na 0. Spočítá jejich
   součet a vrátí jej jako svůj výsledek (return).    
"""

def soucet(x=0, y=0, z=0):
    return x+y+z
