# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012

@author: Radek
"""
"""     Soubory (čtení)
        
readlines() - vrátí seznam řádků souboru od akt. poz.          
readline() - přečte řetězec od aktuální pozice do 
             konce řádku  
read(x) - přečte řetězec o zadané délce, když neuvedeme
          hodnotu, přečte celý soubor
        - při pokusu o čtení na konci souboru vrací
          prázdný řetězec ""
tell() - vrací aktuální pozici v souboru
seek(pocet) - posune aktuální pozici o daný počet
              bytů od začátku souboru

Užitečné textové funkce
splitlines() - jako split, oddělovačem je "\n"
"""


# soub=open("narozeniny.txt","r")
# seznam=soub.readlines()
# soub.close()
# print (seznam)


#Jak se zbavit konců řádků? Např. takto:
#for i in range(len(sez)):
#    sez[i]=sez[i][0:-1]
#print (sez)



# soubor=open("narozeniny.txt","r")
# for i in range(2):
#     soubor.readline()
# radek=soubor.readline()
# soubor.close()
# print(radek)


# soubor=open("narozeniny.txt","r")
# vsechno=soubor.read()
# print (vsechno)
# soubor.close()

#ukázka příkazu tell()
# soubor=open("narozeniny.txt","r")
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# text=soubor.read(10)
# print(text)
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# soubor.close()


#ukázka příkazu seek()
# soubor=open("narozeniny.txt","r")
# soubor.seek(11)
# text=soubor.readline()
# print (text)
# soubor.close()


#ošetření otvírání a práce s koncem souboru
# try:
#     soubor=open("narozeniny.txt","r")
#     radek=soubor.readline()
#     while radek!="":
#         print(radek,end="")
#         radek=soubor.readline()
#     soubor.close()
# except:
#     print("Chyba při otvírání souboru!")


"""
Úkoly:
1) Otevřete soubor pokus.txt a vypište jeho 
   obsah do souboru kopie.txt. 
    Použijte buď readlines + writelines nebo read + write.
2) Přečtěte soubor PISMENA.TXT pomocí příkazu read(1) a 
   zjistěte, kolik je v něm písmen "a".
3) Vygenerujte soubor VSTUP.TXT, ve kterém budou dva
   sloupce dvojciferných čísel oddělené mezerou. V
   každém bude 100 čísel.
   VSTUP.TXT:
   12 35\n
   43 71\n
   10 99\n
   ...
     
   Tento soubor postupně přečtěte a do souboru SOUCTY.TXT
   vypište řádkové součty ve formátu a+b=c.
   SOUCTY.TXT:
   12+35=47\n
   43+71=114\n
   10+99=109\n
   ...
   
4) Načtěte ze souboru řetězec o délce 10 znaků,
   který představuje datum a otestujte správnost 
   jeho formátu (dd.mm.rrrr). Jen formát, hodnoty čísel
   nemusí být pravdivé.
5) Načtěte od uživatele 5 řetězců do seznamu, ke každému
   přidejte \n a pomocí operace WRITELINES zapište seznam
   do souboru.
6) Pokuste se otevřít neexistující soubor v módu "a" a
   přidat na konec krátký text.
7) Otevřete nějaký soubor pro čtení a spočítejte, kolik má
   znaků. (Nápověda - přečtěte soubor jako jeden celý
   řetězec a zjistěte jeho délku)
8) V souboru neznámé délky jsou na řádcích údaje:
   věk - jméno
   věk - jméno
   ...
   Čtěte ze souboru data a zjistěte jméno nejstaršího člověka.
   Vypište jej na obrazovku. Můžete využít operaci split().
   Věk může být až trociferný.
"""

























import random as r
soubor = open("vstup.txt","w")
for i in range(100):
    a = r.randint(10, 99)
    b = r.randint(10, 99)
    vystup = "{} {}\n".format(a,b)
    soubor.write(vystup)
soubor.close()

vstup = open("vstup.txt","r")
vystup = open("soucty.txt","w")
radek = vstup.readline()
while radek != "":
    a = int(radek[:2])
    b = int(radek[3:5])
    c = a + b
    vystup.write("{}+{}={}\n".format(a,b,c))
    radek = vstup.readline()
vstup.close()    
vystup.close()


# soubor = open("lidi.txt")
# data = soubor.readlines()
# soubor.close()
# nej_vek = 0
# nej_jmeno = ""

# for radek in data:
#     dvojice = radek.split("-")
#     vek = int(dvojice[0])
#     jmeno = dvojice[1]
#     if vek > nej_vek:
#         nej_vek = vek
#         nej_jmeno = jmeno

# print(nej_vek, nej_jmeno)








