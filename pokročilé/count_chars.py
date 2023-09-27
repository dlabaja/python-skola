from string import ascii_lowercase
from sys import stdin, stdout, stderr
import unicodedata
import math

def percent_to_text(percent):
    return "#" * percent

def sum_values(char_dict):
    result = 0
    for i in char_dict.values():
        result += i
    return result

# input = unicodedata.normalize("NFKD", input("Zadejte vstup: ")).encode("ascii", "ignore").decode("ascii")
input = unicodedata.normalize("NFKD", stdin.read()).encode("ascii", "ignore").decode("ascii")

chars = {}

# init chars dict
for i in ascii_lowercase:
    chars[i] = 0

for i in input:
    if i in chars:
        chars[i] += 1

sum = sum_values(chars)
for k, v in chars.items(): # sorted(chars.items(), key=lambda x:x[1], reverse=True):
    print(f"{k}: {v:{len(str(sum))}d} ({v/sum*100:5.1f} %) {percent_to_text(round(v/sum*100))}") # 'a:  74 (  7.6 %) ########'