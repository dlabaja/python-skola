# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:10:45 2013

@author: Radek

"""
"""
Možnosti programování:
1) Idle - součást každé instalace Pythonu, stačí, ale je nutno mít otevřeno mnoho oken
2) Spyder - výhodnější práce, používá panely
3) www.replit.com - online
4) Visual Studio Code (Codium)
5) PyCharm  - profesionální a hodně složitý nástroj
"""

"""
Výukové materiály
http://www.sallyx.org/sally/python/
https://mamut.spseol.cz/nozka/python/
http://howto.py.cz/index.htm
http://diveintopython3.py.cz/index.html  - kompletní dokumentace k Pythonu
https://python.cz/zacatecnici/           - spousta různých návodů a odkazů

Python pro samouky
https://krython.vnovak.cz/           - samostatná výuka s úkoly (jednoduché)
https://www.sololearn.com/           - samostatná výuka s úkoly (různé úrovně a jazyky)
https://www.w3schools.com/python/exercise.asp
https://www.itnetwork.cz/e-learning-profese/junior-programator/python



Výstup na obrazovku
print ("text")  - vypíše do výstupu zadaný řetězec (text) 
                  a přejde na nový řádek
print ("\n")    - přechod na nový řádek
print ("\t")    - odskok o tabulátor
print ()        - prázdný řádek
print ("text",end="") - neproběhne zalomení po printu


Komentáře
# jednořádkový komentář
""" 

"""
  víceřádkový 
  komentář 
"""

"""
Matematické operace
+  sčítání
-  odčítání
*  násobení
/  dělení
// celočíselné dělení
%  zbytek po dělení
** umocňování

Čísla
celá (např. 15)
desetinná (př. 3.141) - tečka
komplexní (př. 5+4j) - bez mezer
"""


print("10+5=",10+5)
print("45-12=",45-12)
print(-8*3.12)

# print(11/4)
# print(11//4)
# print(11%4)

# print(2**10000)

# print((5+4j)/(6-2j))

"""
Úkol:
1) Napište pod sebe čísla 1-5 diagonálně:
   1
    2
     3    
      ...
"""

for i in range(5):
    s = ""
    for _ in range(i):
        s += " "
    print(f"{s}{i + 1}")

"""     
2) Máte 3 zrnka pšenice. Jedno zrnko váží
   0,05g. Z každého vyroste
   12 nových zrn. Za rok se stihnou
   2 úrody. Jak velká úroda v kg bude
   za tři roky?
       
"""

print(f"{3 * 12**6 * 0.00005}kg/{3 * 12**6} semen")



















