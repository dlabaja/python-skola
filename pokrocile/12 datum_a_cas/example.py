import datetime

# Získání aktuálního data a času
aktualni_datum_a_cas = datetime.datetime.now()
print("Aktuální datum a čas:", aktualni_datum_a_cas)


# Vytvoření vlastního data a času
datum = datetime.date(2024, 4, 16)
cas = datetime.time(12, 30, 15)
print("Vlastní datum:", datum)
print("Vlastní čas:", cas)


# Přidání času k datu
novy_datum = datum + datetime.timedelta(days=5)

# Porovnání dat
if datum > datetime.date(2024, 4, 10):
    print("Datum je pozdější než 10. dubna 2024.")

# Formátování dat a časů
print(aktualni_datum_a_cas.strftime("%Y-%m-%d %H:%M:%S"))  # Formátování do řetězce


datum_str = "2024-04-16"
cas_str = "12:30:15"
datum_z_retezce = datetime.datetime.strptime(datum_str, "%Y-%m-%d")
cas_z_retezce = datetime.datetime.strptime(cas_str, "%H:%M:%S")
print("Datum z řetězce:", datum_z_retezce)
print("Čas z řetězce:", cas_z_retezce)


# List comprehension pro generování dat:
data = [datetime.date.today() + datetime.timedelta(days=i) for i in range(5)]
print(data)

# Využití tuple unpackingu:
rok, mesic, den = datetime.date.today().timetuple()[:3]
print("Rok:", rok, "Mesic:", mesic, "Den:", den)

# Formátování data a času pomocí f-stringu:
print(f"Dnes je {datetime.date.today():%A, %d. %B %Y}")


# Zjištění počtu dní v měsíci:
aktualni_mesic = datetime.date.today().month
pocet_dni = (datetime.date(datetime.date.today().year, aktualni_mesic % 12 + 1, 1) - datetime.timedelta(days=1)).day
print("Počet dní v aktuálním měsíci:", pocet_dni)
