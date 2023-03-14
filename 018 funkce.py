import random

def AnaX(a, x):
    print(a ** x)


def linear(a, b):
    print((-b)/a)


def prumer(a, b, c):
    return (a + b + c)/2


def kostka():
    return random.randint(1, 6)


def vrat_seznam(pocet, od, do):
    if pocet < do:
        print("Parametr 'do' musí být <= parametru 'pocet'")
        return
    seznam = []
    for _ in range(pocet):
        seznam.append(random.randint(0, 100))
    return seznam[od:do + 1]


def zasifruj_text(text):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for i in range(len(text)):
        output += f"{i}{abeceda[random.randint(0, len(abeceda))]}"