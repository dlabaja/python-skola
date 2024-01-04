from game import *

def assign_rules():
    input("Zadejte počet řádků hry")

def handle_numeric_input(input_msg, lower_bound_inclusive, upper_bound_inclusive):
    while True:
        s = input(input_msg)
        if s.isdecimal():
            return int(s)
        else:
            print(
                f"Neplatná číselná hodnota, číslo musí být >= {lower_bound_inclusive} a zároveň <= {upper_bound_inclusive}")

def handle_input(input_msg):
    while True:
        s = input(input_msg)
        if len(s) > 0 and not s.isspace():
            return s
        else:
            print(f"Neplatný vstup")

if __name__ == '__main__':
    while True:
        row_count = handle_numeric_input("Zadejte počet řádků (3 - 20): ", 3, 20)
        column_count = handle_numeric_input("Zadejte počet sloupců (3 - 20): ", 3, 20)

        players = []
        player_count = handle_numeric_input("Zadejte počet hráčů: ", 1, 7)
        for i in range(player_count):
            players.append(handle_input(f"Zadejte jméno hráče č. {i + 1}: "))

        g = Game(players, row_count, column_count)