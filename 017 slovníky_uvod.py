# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:57:07 2012

@author: Radek
"""
"""
Slovníky (dictionary, hash, asociativní pole)
- vytvářejí se pomocí {}
- položky mají tvar INDEX(KLÍČ):HODNOTA
- indexovat můžeme pomocí lib. jednoduch. dat. typu
- indexy musí být unikátní
- k hodnotám se přistupuje pomocí klíčů
- oproti seznamům mají mnohonásobně rychlejší přístup
  k datům
"""

#Praktická ukázka
# barvy={"cervena":"#ff0000", "zelena":"#00ff00"}
# print(barvy)
# print(barvy["cervena"])
       


slovnik={5:'pětka',1:"jednička",3:"trojka",2:"dvojka",4:"čtyřka"}
print (slovnik)

# for i in slovnik:
#     print (slovnik[i])

klic=6
hodnota="šestka"
slovnik[klic]=hodnota
print (slovnik)
#vložení nového klíče a hodnoty



del slovnik[6]
print (slovnik)


#keys() - vrátí seznam klíčů ze slovníku
#values() - vrátí seznam hodnot
#pomocí operace in zjistíme, zda je hodnota uvnitř
#slovníku

# print (list(slovnik.keys()))
# print (list(slovnik.values()))
print (6 in slovnik)


"""
Úkol:
1) Vytvořte si jednoduchý anglicko-český překladový 
   slovník, který obsahuje 5 položek.
   Pokuste se pomocí něj překládat uživatelské vstupy,
   pokud zadané slovo nebude ve slovníku, oznamte to
   uživateli.
2) Vytvořte si slovník přátel. Klíčem budou křestní
   jména, hodnotou bude seznam osobních údajů.
   Pomocí cyklu vypište pod sebe všechny osoby ze slovníku.
   ve tvaru:
   jmeno1 => [osobní údaje]    
   jmeno2 => [osobní údaje]
   ...   
"""   




