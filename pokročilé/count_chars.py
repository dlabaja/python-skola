from string import ascii_lowercase
import unicodedata
import math

def percent_to_text(percent):
    return "#" * round(percent / 2)

# input = unicodedata.normalize("NFKD", input("Zadejte vstup: ")).encode("ascii", "ignore").decode("ascii")
input = "sussy suspppp"

chars = {}
char_count = 0

for i in ascii_lowercase:
    chars[i] = 0

for i in input:
    try:
        chars[i] += 1
        char_count += 1
    except KeyError:
        continue

for k, v in sorted(chars.items(), key=lambda x:x[1], reverse=True):
    print(f"{k}: {v} ({round(v/char_count*100):2d} %) {percent_to_text(round(v/char_count*100))}")

