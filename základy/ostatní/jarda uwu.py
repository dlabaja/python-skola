import math

def trojuhelnik():
    a = int(input("Zadejte stranu a: "))
    b = int(input("Zadejte stranu b: "))
    c = int(input("Zadejte stranu c: "))
    obvod = a + b + c
    s = (a + b + c) / 2
    obsah = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Trojúhelník má obvod {obvod} cm a obsah {round(obsah, 2)} cm")

def kvadr():
    a = int(input("Zadejte stranu a: "))
    b = int(input("Zadejte stranu b: "))
    c = int(input("Zadejte stranu c: "))
    objem = a * b * c
    povrch = 2*(a*b+a*c+b*c)
    print(f"Kvádr má objem {objem} cm a povrch {povrch} cm")

def vypocet_delky():
    mm = int(input("Zadejte počet milimetrů: "))
    m = math.floor(mm/1000)
    cm =  math.floor((mm - m * 1000) / 10)
    mmf = mm - m * 1000 - cm * 10
    print(f"{m} m, {cm} cm a {mmf} mm")

def pythagorovka():
    c = int(input("Zadejte přeponu: "))
    b = int(input("Zadejte odvěsnu: "))
    a = math.sqrt(math.pow(c, 2) - math.pow(b, 2))
    print(f"Druhá odvěsna má {a} cm")

def pet_cisel():
    a = int(input("Zadejte číslo 1: "))
    b = int(input("Zadejte číslo 2: "))
    c = int(input("Zadejte číslo 3: "))
    d = int(input("Zadejte číslo 4: "))
    e = int(input("Zadejte číslo 5: "))
    soucet = a + b + c + d + e
    prumer = soucet / 5
    print(f"Součet je {soucet}, průměr je {prumer}")