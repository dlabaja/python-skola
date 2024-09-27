from main_game.block import Block
import random


class Game:
    current = None

    def __init__(self):
        Game.current = self
        self.blocks = []
        self.ended = False
        self.map = [[None] * 4 for _ in range(4)]
        self.score = 0
        self.score_locked = False

    def add_block(self, pos, value=2):
        block = Block(pos)
        block.value = value
        self.blocks.append(block)

        if self.map[pos[1]][pos[0]] is not None and self.map[pos[1]][pos[0]].value == value:
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

    def move_block(self, block, new_pos):
        self.map[block.pos[1]][block.pos[0]] = None
        self.map[new_pos[1]][new_pos[0]] = block
        block.pos = new_pos

    def merge_blocks(self, block_to_keep, block_to_remove):
        block_to_keep.value *= 2
        self.blocks.remove(block_to_remove)
        self.map[block_to_remove.pos[1]][block_to_remove.pos[0]] = None
        self.map[block_to_keep.pos[1]][block_to_keep.pos[0]] = block_to_keep

        if not self.score_locked:
            self.score += block_to_keep.value

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

        self.score_locked = True
        self.add_block(ls[random.randint(0, len(ls) - 1)])
        self.score_locked = False

    def move_blocks_down(self):
        _map = [row[:] for row in self.map]
        for x in range(4):
            blocks = []
            for y in range(4):
                blocks.append(self.map[4 - (y + 1)][x])

            self.__move_blocks__(blocks, [0, 1])

        if _map != self.map:
            return True
        return False

    def __move_blocks__(self, blocks, next_block_offset):
        from main_game.controls import Controls
        if Controls.has_no_moves():
            self.ended = True
            return

        i = 0
        for block in blocks:
            if block is None:
                i += 1
                continue

            for _ in range(i):
                pos = block.pos
                next_block = self.map[pos[1] + next_block_offset[1]][pos[0] + next_block_offset[0]]
                next_block_pos = [pos[0] + next_block_offset[0], pos[1] + next_block_offset[1]]
                if next_block is None:
                    self.move_block(block, next_block_pos)
                elif (next_block is not None
                      and next_block.value == block.value):
                    self.merge_blocks(next_block, block)
                else:
                    break
            i += 1

    def move_blocks_right(self):
        _map = [row[:] for row in self.map]
        for y in range(4):
            blocks = []
            for x in range(4):
                blocks.append(self.map[y][4 - (x + 1)])

            self.__move_blocks__(blocks, [1, 0])

        if _map != self.map:
            return True
        return False

    def move_blocks_left(self):
        _map = [row[:] for row in self.map]
        for y in range(4):
            blocks = []
            for x in range(4):
                blocks.append(self.map[y][x])

            self.__move_blocks__(blocks, [-1, 0])

        if _map != self.map:
            return True
        return False

    def move_blocks_up(self):
        _map = [row[:] for row in self.map]
        for x in range(4):
            blocks = []
            for y in range(4):
                blocks.append(self.map[y][x])

            self.__move_blocks__(blocks, [0, -1])

        if _map != self.map:
            return True
        return False
