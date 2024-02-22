from main_game.block import Block
import random

class Game:
    current = None
    def __init__(self):
        Game.current = self
        self.blocks = []
        self.ended = False
        self.map = [[None] * 4 for _ in range(4)]

    def add_block(self, pos):
        block = Block(pos)
        self.blocks.append(block)

        if self.map[pos[1]][pos[0]] is not None:
            self.merge_blocks(self.map[pos[1]][pos[0]], block)
            return

        self.map[pos[1]][pos[0]] = block
        return block

    def get_block_value(self, x, y):
        if self.map[y][x] is None:
            return ""

        return str(self.map[y][x].value)

    def remove_block(self, block):
        self.blocks.remove(block)

    def merge_blocks(self, block_to_keep, block_to_remove):
        block_to_keep.value *= 2
        self.blocks.remove(block_to_remove)

    def get_free_cells(self):
        ls = []
        for y in range(4):
            for x in range(4):
                if self.map[y][x] is None or self.map[y][x].value == 2:
                    ls.append([x, y])
        return ls

    def next_turn(self):
        ls = self.get_free_cells()
        if len(ls) == 0:
            self.ended = True
            return

        self.add_block(ls[random.randint(0, len(ls) - 1)])
