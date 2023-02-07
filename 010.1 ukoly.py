def uroky():
    penize = int(input("Zadejte počet peněz: "))
    urok = int(input("Zadejte úrok v %: "))
    roky = int(input("Zadejte počet let: "))
    i = 1
    ucet = penize
    while i <= roky:
        ucet += ucet * (urok/100)
        print(f"{i}. rok: {round(ucet, 2)}")
        i += 1 



def sirky():
    sirky = 21
    tah = 1
    while sirky > 1:
        print(f"""-------------------
Na tahu je {get_hrac(tah)}
Počet sirek je nyní {sirky}""")

        sirky -= verify_input()
        if sirky < 1:
            break

        tah += 1
    print(f"{get_hrac(tah)} prohrál")

def get_hrac(tah):
    if tah % 2 == 0:
        return "Hráč č.2"
    return "Hráč č.1"

def verify_input():
    vstup = input("Zadejte počet sirek (1-3): ")
    while try_parse_int(vstup) == None or try_parse_int(vstup) < 1 or try_parse_int(vstup) > 3:
        print("Wrong number, try again")
        vstup = input("Zadejte počet sirek (1-3): ")
    return int(vstup)

def try_parse_int(string):
    try:
        return int(string)
    except Exception:
        return None

sirky()