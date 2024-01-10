from game_objects import *
import renderer

reset_style = "\u001b[0m"
yellow = "\u001b[1;93m"
red = "\u001b[1;31m"
green = "\u001b[1;92m"

class Game:
    def __init__(self, player_names: list, row_count, column_count):
        self.map_length = row_count * column_count
        self.fields = []
        self.players = []

        self.generate_map()

        for i in range(len(player_names)):
            self.players.append(Player(player_names[i]))

        self.play(row_count)

    def play(self, row_count):
        while True:
            for player in self.players:
                renderer.print_map(self.fields, self.players, row_count)

                input(f"Na tahu je hráč {yellow}{player.name}{reset_style}. Stiskněte ENTER pro hod kostkou.")
                dice = self.throw_dice()

                print(
                    f"{yellow}{player.name}{reset_style} hodil {yellow}{dice}{reset_style}, nyní je na poli {yellow}{player.position + 1 + dice}{reset_style}")

                # further than last field
                if player.position + dice > len(self.fields) - 1:
                    print(f"{red}Přestřelil jsi mapu, zkus to příště.{reset_style}")
                    continue

                player.position += dice

                if player.position == self.map_length - 1:
                    self.end_game(player)
                    return

                # teleporting
                while player.position != self.fields[
                    player.position].teleport_index:  # teleporting until the field is no longer spacial
                    if isinstance(self.fields[player.position], Snake):
                        print(
                            f"Ale ne, na poli je {red}had{reset_style} a {yellow}{player.name}{reset_style} padá na pole č. {yellow}{self.fields[player.position].teleport_index + 1}{reset_style}")
                    elif isinstance(self.fields[player.position], Ladder):
                        print(
                            f"Hurá, po {green}žebříku{reset_style} jsi vyšplhal až na pole č. {yellow}{self.fields[player.position].teleport_index + 1}{reset_style}")
                    player.position = self.fields[player.position].teleport_index

                input("Stiskni ENTER pro předání kostky.")

    def end_game(self, player):
        print("====================================")
        print(f"{yellow}{player.name}{reset_style} vyhrál hru, dostal se až na poslední políčko.")
        print("====================================")
        return

    def generate_map(self):
        for i in range(self.map_length):
            if random.randint(0,
                              6) == 0 and 1 < i < self.map_length - 1:  # spawn chance, no spawn at first and last fields
                if random.randint(0, 1) % 2 == 0:
                    self.fields.append(Ladder(i, self.map_length))
                    continue
                self.fields.append(Snake(i))
                continue
            self.fields.append(Field(i))

    @staticmethod
    def throw_dice():
        count = 0
        while True:
            dice = random.randint(1, 6)
            count += dice
            if dice != 6:
                return count
            else:
                input(f"Hodil jsi {yellow}6{reset_style}, házíš znovu!")
