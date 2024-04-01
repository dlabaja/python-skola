import unicodedata
from string import ascii_lowercase
from sys import stdin, stdout
import click

alphabet = ascii_lowercase

@click.command()
@click.option("-i", "--input", default="-", help="Path to the input file. Leave empty for terminal input")
@click.option("-s", "--shift", default=1, help='Shift of the cipher')
@click.argument("output", default=stdout, type=click.File('w'), required=True)

def handle_command(input, shift, output):
    if input == '-':
        print("Zadejte slovo k (de)šifrování: ")
        input = unicodedata.normalize("NFKD", stdin.read()).encode("ascii", "ignore").decode("ascii").lower()
        print()
    else:
        input = unicodedata.normalize("NFKD", input).encode("ascii", "ignore").decode("ascii").lower()

    caesar = cipher(input, shift, output)

    output.write(caesar)
    if output == stdout:
        print()

def cipher(input, shift, output):
    caesar = ""
    for c in input:
        if c not in alphabet:
            caesar += c
            continue
        caesar += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
    return caesar

if __name__ == '__main__':
    handle_command()