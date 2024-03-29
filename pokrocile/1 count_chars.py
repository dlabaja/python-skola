from string import ascii_uppercase
from sys import stdin, stdout, stderr, argv
import unicodedata
import math

def percent_to_text(percent):
    return "#" * percent

def sum_values(char_dict):
    result = 0
    for i in char_dict.values():
        result += i
    return result

if len(argv) > 1:
    input = open(argv[1]).read().upper()
else:
    stdout.write("Zadejte vstup: ")
    # input = unicodedata.normalize("NFKD", input("Zadejte vstup: ")).encode("ascii", "ignore").decode("ascii")
    input = unicodedata.normalize("NFKD", stdin.read()).encode("ascii", "ignore").decode("ascii").upper()

chars = {}

# init chars dict
for i in ascii_uppercase:
    chars[i] = 0

for i in input:
    if i in chars:
        chars[i] += 1

sum = sum_values(chars)
for k, v in chars.items(): # sorted(chars.items(), key=lambda x:x[1], reverse=True):
    print(f"{k}: {v:{len(str(sum))}d} ({v/sum*100:5.1f} %) {percent_to_text(round(v/sum*100))}") # 'a:  74 (  7.6 %) ########'