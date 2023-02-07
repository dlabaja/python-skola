# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 @author: Radek
"""
"""
        Seznamy a jejich operace
append(hodnota)       - přidá hodnotu na konec seznamu
count(hodnota)        - zjistí počet výskytů dané hodnoty
insert(index, hodnota)- vloží hodnotu na pozici v seznamu
pop(index)            - odebere prvek z dané pozice
remove(hodnota)       - odebere první výskyt této hodnoty
sort()                - setřídí seznam podle velikosti

delka=len(seznam)     - zjištění velikosti seznamu
""" 


# seznam=[100,2012,1000,3,1,500,17]
# seznam=seznam+[2012]
# seznam.append(2012) 
# print (seznam)


# print ("Pocet 2012: ",seznam.count(2012))


# seznam.insert(-10,"Vlozeno") #vloží hod. na začátek
# print (seznam)


# #Pokud neuvedeme index, odebírá z konce seznamu
# x=seznam.pop(0) #Odebere prvek z pozice 0
# print (x)
# print (seznam)


# seznam.remove(2012) #Odebere první výskyt
# print (seznam)


# seznam.sort()
# print (seznam)


# ret=["beta","c","a","alfa"]
# ret.sort()
# print(ret)


# print(*ret)
# print("beta","c","a","alfa")


# print ("Seznam má",len(ret),"prvků.")


"""
Úkol:
1) Napište cyklus, který bude načítat z klávesnice 5 
   čísel a postupně je bude dávat na konec prázdného 
   seznamu. Seznam nakonec vypište.
"""

def cyklus():
   seznam = []
   for i in range(5):
      seznam.append(int(input(f"Zadejte hodnotu dalšího prvku: ")))
   print(seznam)

"""
2) Vygenerujte a vypište seznam 20-ti náhodných čísel.
"""

import random

def rand():
   seznam = []
   for i in range(20):
      seznam.append(random.randint(0,100))
   print(seznam)

"""
3) Vygenerujte seznam 20-ti náh. čísel od 1 do 10,
   seznam setřiďte a vytvořte k němu seznam druhých
   mocnin. Oba seznamy vypište.
"""

def mocniny():
   cisla = []
   for i in range(20):
      cisla.append(random.randint(1,10))
   cisla.sort()

   mocniny = []
   for i in range(20):
      mocniny.append(cisla[i] * cisla[i])
   print(f"Čísla: {cisla}")
   print(f"Mocniny: {mocniny}")
   return mocniny

"""
4) Zjistěte, kolikrát se v mocninách vyskytuje 81.
   Odstraňte všechna čísla 81 ze seznamu mocnin.
"""

def odstranit():
   seznam = []
   seznam = mocniny()
   print(seznam.count(81))
   print(list(filter((81).__ne__, seznam)))

""" 
5) Uložte do seznamu 6 náhodných hodů kostkou a zjistěte,
   jestli padla postupka tj. všechny hodnoty od 1 do 6.
"""

def kostka():
   seznam = []
   for _ in range(6):
      seznam.append(random.randint(1,6))
   print(seznam)
   if(len(seznam) != len(set(seznam))):
      return False
   return True

def kostka2():
   i = 1
   while not kostka():
      i += 1
   print(i)

"""
6) Do seznamu "karty" vložte názvy karet. Vytvořte seznam
   "balicek" a vložte do něj zamíchané názvy karet.
   Help: karty=["♥7","♦7","♣7","♠7", ...]
"""

def karty():
   karty = []
   typy = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
   barvy = ["♥", "♦", "♣", "♠"]
   for typ in range(13):
      for barva in range(4):
         karty.append(f"{barvy[barva]}{typy[typ]}")
   karty += ["ŽO"] * 2
   random.shuffle(karty)
   print(karty)

"""
7) Napište simulaci sportky. Člověk zadá 6 čísel, poté 
   počítač vylosuje také 6 čísel a vypíše, kolik čísel
   jsme uhádli. Čísla  musí být z intervalu 1-49. Čísla
   se nesmí opakovat.
"""

def sportka():
   min_int = 1
   max_int = 10
   cisla_uzivatel = []
   for i in range(6):
      vstup = int(input(f"Zadejte číslo #{i + 1}: "))
      while vstup in cisla_uzivatel or min_int > vstup or  max_int < vstup:
         vstup = int(input(f"Zadejte číslo od {min_int} - {max_int} nebo to, které jste ještě nezaškrtli"))
      cisla_uzivatel.append(vstup)

   cisla_pc = []
   for _ in range(6):
      vstup = random.randint(min_int, max_int)
      while vstup in cisla_pc:
         vstup = random.randint(min_int, max_int)
      cisla_pc.append(vstup)

   print(f"Uživatel: {cisla_uzivatel}\nPC: {cisla_pc}")
   print(f"Uhádli jste {len(prunik(cisla_uzivatel, cisla_pc))} čísla/čísel!")   

def prunik(lst1, lst2):
    return list(set(lst1) & set(lst2))

"""
DU) 
1) Naprogramujte jakoukoli hru s kostkami pro alespoň dva 
   hráče, jeden z nich bude počítač. 
2) Hra musí být dostatečně složitá a pro pro uchování hodů 
   bude používat seznamy. Příliš jednoduché hry budou vráceny
   k přepracování.
3) Musí být zobrazena pravidla.
4) Hra po spuštění zobrazí jednoduché textové menu:
   
   1) Zobraz pravidla
   2) Hrát hru
   3) Konec
   Zadej svou volbu:
       
   Po ukončení hry se program vrací do menu, nedojde k ukončení
   aplikace!
5) Hody hráčů (člověka i počítače) musí proběhnout až po stisku 
   klávesy Enter! 
   Použijte tento příkaz, který v podstatě způsobí čekání programu, 
   dokud uživatel nestiskne Enter: input("Stiskni Enter...").
   Snažte se o přehledné výpisy stavu hry - např. průběžné body
   za kolo a také celkové od začátku hry.
6) Každý musí mít jinou hru! :)   
""" 
