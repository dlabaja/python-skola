# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 08:16:48 2012

@author: Martin
"""
"""
Proměnné
- slouží k uchovávání hodnot, výsledků, ...
- jmenují se podle toho, co obsahují!!!
- můžeme je přímo použít
- názvy mohou obsahovat:
    malá písmena (bez diakritiky)
    velká písmena
    číslice (nesmí začínat číslicí)
    podtržítko
- nelze použít klíčová (vyhrazená) slova 

Přiřazovací příkaz
- umožňuje vkládat do proměnné hodnotu
- původní hodnota proměnné se ztratí!
- proměnná je vždy vlevo a výraz vpravo
Např:
a=10
a=b=c=1    vícenásobné přiřazení

Zkrácená přiřazení
+=, -=, *=, /=
a+=1   stejné jako a=a+1
"""


# cislo = 15
# print("Hodnota proměnné je",cislo)
# cislo = 50      #přepis hodnoty na novou
# print("Nová hodnota je",cislo)



a=7
print("Původní hodnota proměnné a:",a)
a=a+3
print("Nová hodnota proměnné a:",a)


a=10
print ("Původní hodnota:",a)
a+=5 
print ("Nová hodnota:",a)



# a=3
# b=10
# soucet=a+b
# rozdil=a-b
# soucin=a*b
# podil=a/b
# celociselny_podil=a//b
# zbytek=a%b
# mocnina=a**b

# print("a =",a,"b =",b)
# print("a+b =",soucet)
# print("a-b =",rozdil)
# print("a*b =",soucin)
# print("a/b =",podil)
# print("a//b =",celociselny_podil)
# print("a%b =",zbytek)
# print("a**b =",mocnina)


"""
Úkol:
1) Zvolte si a=5 a b=2 a vypočítejte hodnotu 
   vyrazu a/b + b/a. Výsledek 2.9.
2) Převeďte číslo FAD z hexadecimálního na 
   desítkové. Použijte proměnné!
   Výsledek 4013. 
"""

print(5/2 + 2/5)
a = 5
b = 6
c = 7
print(a * b *c) 













