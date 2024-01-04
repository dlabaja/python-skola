import random
from enum import Enum

class FieldColor(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4

class Field:
    def __init__(self, index, teleport_index=None):
        self.index = index
        # self.color = generate_color()

        if teleport_index is None:
            self.teleport_index = index
        else:
            self.teleport_index = teleport_index

    def generate_color(self):
        return

class Player:
    position = 0

    def __init__(self, name):
        self.name = name

class Ladder(Field):
    def __init__(self, index, map_length):
        teleport_index = random.randint(index, map_length - 1)
        super().__init__(index, teleport_index)

class Snake(Field):
    def __init__(self, index):
        teleport_index = random.randint(0, index - 1)
        super().__init__(index, teleport_index)
