from game_objects import *
import renderer

class Game:
    fields = []
    players = []

    def __init__(self, player_names: list, row_count, column_count):
        self.map_length = row_count * column_count
        if self.map_length > 400: raise Exception("To pole je nějaké velké, takový terminál určitě nemáš :)")

        self.generate_map()

        for i in range(len(player_names)):
            self.players.append(Player(player_names[i]))

        self.play(row_count)

    def play(self, row_count):
        while True:
            for player in self.players:
                renderer.print_map(self.fields, self.players, row_count)

                input(f"Na tahu je hráč {player.name}. Stiskněte ENTER pro hod kostkou.")
                dice = self.throw_dice()
                player.position += dice

                if player.position >= self.map_length:
                    self.end_game()
                    return

                print(f"Hráč hodil {dice}, nyní je na poli {player.position + 1}")

                # teleporting
                while player.position != self.fields[player.position].teleport_index:  # teleporting until the field is no longer spacial
                    if isinstance(self.fields[player.position], Snake):
                        print(f"Ale ne, na poli je had a hráč padá na pole č. {self.fields[player.position].teleport_index + 1}")
                    elif isinstance(self.fields[player.position], Ladder):
                        print(f"Hurá, po žebříku jsi vyšplhal až na pole č. {self.fields[player.position].teleport_index + 1}")
                    player.position = self.fields[player.position].teleport_index

                input("Stiskni ENTER pro předání kostky.")

    def end_game(self):
        print(f"Hráč vyhrál hru, dostal se na konec.")
        return

    def generate_map(self):
        for i in range(self.map_length):
            if random.randint(0, 6) == 0:
                if random.randint(0, 1) % 2 == 0:
                    self.fields.append(Ladder(i, self.map_length))
                    continue
                self.fields.append(Snake(i))
                continue
            self.fields.append(Field(i))

    @staticmethod
    def throw_dice():
        return random.randint(1, 6)
