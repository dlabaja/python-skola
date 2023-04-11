# skupina A
"""
Test – měsíce
Vytvořte skript, který bude k číslům zobrazovat správný měsíc.

Zadání:
•	Vygenerujte si desetiprvkový seznam náhodných čísel z intervalu <1,12>
•	Vytvořte si pomocný slovník, kde čísla budou klíče a názvy měsíců budou hodnoty (např. klíč=1 a odpovídající hodnota=“leden“)
•	Následně projděte celý vygenerovaný seznam, vypište jeho prvky a s pomocí vašeho slovníku k nim přidejte odpovídající názvy podle následujícího vzoru.
Př:
Seznam: [2,8,9,4,3,6,1,0,5,7]
Přepis:
2: unor
8: srpen
9: zari
4: duben
…
…
7: cervenec
"""
import random

def mesice():
    seznam = []
    mesice = {1:"leden", 2:"únor", 3:"březen", 4:"duben", 5:"květen", 6:"červen", 7:"červenec", 8:"srpen", 9:"září", 10:"říjen", 11:"listopad", 12:"prosinec"}
    for _ in range(10):
        seznam.append(random.randint(1,12))
    print(f"Seznam: {seznam}\nPřepis:")
    for item in seznam:
        print(f"{item}: {mesice[item]}")

mesice()
