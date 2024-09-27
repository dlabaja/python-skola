with open("pokročilé/prace_se_soubory/soubor.txt", "w") as file:
    c = ord("a")
    while chr(c) != "z":
        file.write(chr(c))
        c += 1

    file.write("sus\n")
    file.write("amogus")

print("Soubor vytvořen")

with open("pokročilé/prace_se_soubory/soubor.txt", "r") as file:
    znak = file.read(1)
    tri_znaky = file.read(3)
    radek = file.readline()
    zbytek = file.read()
    file.seek(0) # kurzor na začátek

print(znak, tri_znaky, radek, zbytek)

