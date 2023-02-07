'''
Napište program, který vypíše prvních n řádků násobilky zvoleného čísla x. Tyto dvě hodnoty načtěte z klávesnice. Jestliže n bude zadáno menší než 1, program vypíše chybu a k výpisu násobilky nedojde. Hodnota x může být libovolná.

Př. 1: 
Zadejte číslo: 8
Zadejte počet řádků: 4

1 x 8 = 8
2 x 8 = 16
3 x 8 = 24
4 x 8 = 32

Př. 2: 
Zadejte číslo: 8
Zadejte počet řádků: -4

Chyba v poctu radku!
'''

def nasobilka():
    vstup = int(input("Zadejte číslo: "))
    radky = int(input("Zadejte počet řádků: "))
    if radky < 1:
        print("Chyba v počtu řádků")
        return
    for i in range(radky):
        print(f"{i + 1} x {vstup} = {(i+1)*vstup}")

nasobilka()

