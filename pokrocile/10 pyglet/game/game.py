from game.block import Block


class Game:
    current = None

    def __init__(self):
        current = self
        self.blocks = []

    def add_block(self, pos):
        block = Block(pos)
        self.blocks.append(block)
        return block

    def remove_block(self, block):
        self.blocks.remove(block)

    def merge_blocks(self, block_to_keep, block_to_remove):
        if block_to_remove.value != block_to_keep.value:
            return False

        block_to_keep.value *= 2
        self.blocks.remove(block_to_remove)
        return True
