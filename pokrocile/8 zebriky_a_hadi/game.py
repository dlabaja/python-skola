from game_objects import *
import renderer

class Game:
    fields = []
    players = []

    fields_str = ""

    def __init__(self, player_names: list, row_count=10, column_count=10):
        self.map_length = row_count * column_count
        if self.map_length > 999: raise Exception("To pole je nějaké velké, takový terminál určitě nemáš :)")

        self.generate_map()
        for i in range(row_count):
            for j in range(column_count):
                print(self.fields_str[i * column_count + j], end="")
            print()

        for i in range(len(player_names)):
            self.players.append(Player(player_names[i]))

        renderer.print_map(self.fields, self.players, row_count)

    def play(self):
        while True:
            for player in self.players:
                player.position += self.throw_dice()
                if player.position >= self.map_length:
                    self.end_game()
                    return
                player.position = self.fields[player.position].teleport_index

    def end_game(self):
        return

    def generate_map(self):
        for i in range(self.map_length):
            if random.randint(0, 6) == 0:
                if random.randint(0, 1) % 2 == 0:
                    self.fields.append(Ladder(i, self.map_length))
                    self.fields_str += "L"
                    continue
                self.fields.append(Snake(i))
                self.fields_str += "S"
                continue
            self.fields.append(Field(i))
            self.fields_str += "/"

    @staticmethod
    def throw_dice():
        return random.randint(1, 6)

if __name__ == '__main__':
    g = Game(["adam", "kamil"])
