import unicodedata
from string import ascii_lowercase
from sys import stdin, stdout, stderr, argv

alphabet = ascii_lowercase

def cypher(msg, shift):
    caesar = ""
    for c in msg:
        caesar += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
    return caesar

try:
    msg = unicodedata.normalize("NFKD", argv[1]).encode("ascii", "ignore").decode("ascii").lower()
    shift = argv[2]
    stdout.write(cypher(msg, shift))
except:
    stderr.write("Invalid parameters")

if len(argv) > 1:
    input = 
    if 
else:
    stdout.write("Zadejte vstup: ")
    input = unicodedata.normalize("NFKD", stdin.read()).encode("ascii", "ignore").decode("ascii").upper()

print(cypher("abc", 0))
print(cypher("abc", -1))

print(decypher("abc", 0))
print(decypher("zab", -1))