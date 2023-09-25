# skupina A

"""
Vyhodnocení testové otázky

Vypište uživateli znění testové otázky s třemi možnostmi (viz příklad). Načtěte z klávesnice číslo odpovědi. Oznamte uživateli jednu z tří možných odpovědí:
•	správná odpověď
•	špatná odpověď
•	zadávejte čísla pouze od 1 do 3


Př.1: 
V kterem roce skoncila 1. svetova valka?
1)1914
2)1918
3)1919
Vase odpoved: 1

Spatne!

Př.2: 
V kterem roce skoncila 1. svetova valka?
1)1914
2)1918
3)1919
Vase odpoved: 4

Zadavejte pouze cisla 1-3!
""" 

otazka = int(input("""Ve kterém roce skončila 1. světová válka?
1)1914
2)1918
3)1919
Vaše odpověď: """))

if otazka == 2:
    print("Správně")
elif otazka == 1 or otazka == 3:
    print("Špatně, vraťe se k panu profesoru Johnovi")
else:
    print("Špatně, zadávejte čísla pouze od 1 do 3")
