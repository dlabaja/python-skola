import random
from enum import Enum

class FieldColor(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4

class Field():
    def __init__(self, index, teleport_index = None):
        self.index = index
        # self.color = generate_color()

        if teleport_index == None:
            self.teleport_index = index
        else:
            self.teleport_index = teleport_index

    def generate_color(self):
        return

class Player():
    position = 0

    def __init__(self, name):
        self.name = name

class Ladder(Field):
    def __init__(self, index, map_length):
        teleport_index = random.randint(index, map_length)
        super().__init__(index, teleport_index)

class Snake(Field):
    def __init__(self, index):
        teleport_index = random.randint(0, index)
        super().__init__(index, teleport_index)

class Game():
    fields = []
    players = []

    fields_str = ""

    def __init__(self, player_names : list, row_count = 10, column_count = 10):
        self.map_length = row_count * column_count
        
        self.generate_map()
        for i in range(row_count):
            for j in range(column_count):
                print(self.fields_str[i*column_count+j], end="")
            print()

        for i in range(len(player_names)):
            self.players.append(Player(player_names[i]))

    def play(self):
        while True:
            for player in self.players:
                player.position += throw_dice()
                if player.position >= self.map_length:
                    self.end_game()
                    return
                player.position = self.fields[player.position].teleport_index
        
    def end_game(self):
        return

    def generate_map(self):
        for i in range(self.map_length):
            if random.randint(0,6) == 0:
                if random.randint(0,1) % 2 == 0:
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
        return random.randint(1,6)

g = Game(["adam", "kamil"])