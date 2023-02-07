# skupina A 

"""
Napište program, který načte z klávesnice tři velikosti paměti (kB, B, b). Hodnoty přepočítejte na bity a sečtěte. 1 kB počítejte jako 1000 B. 1 B má 8 bitů. Výsledek vypište dle následujícího vzoru.

Př: 
Zadejte paměť v kB: 1
Zadejte paměť v B: 2
Zadejte paměť v b: 3

Celkem bitů: 8019
"""

kb = int(input("Zadejte paměť v kb: "))
byte = int(input("Zadejte paměť v bytech: "))
bit = int(input("Zadejte paměť v bitech: "))
print(f"Celkem bitů: {bit + byte*8 + kb*8000}")