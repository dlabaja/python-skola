# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:45:15 2011

@author: Radek
"""
"""
                Seznamy
- uvádějí se v [], jednotlivé hodnoty se oddělují čárkou
- mohou obsahovat libovolná data i další seznamy
- čeština v seznamu?
"""

# seznam=[4,2,7]    #prázdný seznam
# print(seznam)    

# print(*seznam)    #print(4,2,7)

# for prvek in seznam:
#     print(prvek, end=" ")


# seznam=[3,"Python",3.0,[1,0,1],False,1000]
# print(seznam)

# print(seznam[1])
# print(seznam[1][1])

# seznam[2]="Programování" #přiřazení
# print(seznam)

    
# seznam=seznam+seznam #spojování seznamů
# print(seznam)

# seznam=[0]*10 #násobení seznamu konstantou
# print(seznam)

# import random
# seznam=[]
# for i in range(10):
#     seznam+=[random.randint(0,20)]
# print(seznam)


"""seznam=list("Python")
print(seznam)

print (seznam[4:]) #podseznam [4..n]
print (seznam[1:4]) #podseznam [1..3]
print (seznam[1:6:2]) #podseznam [1..5] každý 2. prvek"""


"""
Úkol:
1) Vytvořte 5-ti prvkový seznam obsahující nuly a 
   vypište jej.
   Pomocí cyklu načtěte 5 nových hodnot z klávesnice a 
   přepište nuly v seznamu těmito novými hodnotami.
   Seznam vypište.
"""

def prvky():
   seznam = [0,0,0,0,0]
   for i in range(5):
      seznam[i] = int(input(f"Zadejte hodnotu prvku #{i}: "))
   print(seznam)

"""   
2) Pomocí cyklu najděte v tomtéž seznamu nejmenší 
   prvek.
"""

def nejmensi():
   seznam = [1,2,3,4,-1,-5,10]
   nejmensi = seznam[0]
   for i in range(len(seznam)):
      if seznam[i] < nejmensi:
         nejmensi = seznam[i]
   print(nejmensi) 

"""
3) Zjistěte, jestli se v seznamu nachází hodnota 20.   
"""

def contains():
   seznam = [1,3,5,7,12,20,34]
   print(20 in seznam)



        
