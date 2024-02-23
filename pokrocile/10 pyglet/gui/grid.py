import random

import pyglet
from pyglet import shapes
from main_game.game import Game


class Grid:
    subRectOffset = 10
    tile_colors = {  # hodnota : (fg, bg)
        2: ((119, 110, 101), (238, 228, 218)),
        4: ((119, 110, 101), (237, 224, 200)),
        8: ((249, 246, 242), (242, 177, 121)),
        16: ((249, 246, 242), (245, 149, 99)),
        32: ((249, 246, 242), (246, 124, 95)),
        64: ((249, 246, 242), (246, 94, 59)),
        128: ((249, 246, 242), (237, 207, 114)),
        256: ((249, 246, 242), (237, 204, 97)),
        512: ((249, 246, 242), (237, 200, 80)),
        1024: ((249, 246, 242), (237, 197, 63)),
        2048: ((249, 246, 242), (237, 194, 46))
    }

    def __init__(self, length, x, y):
        self.length = length
        self.anchor_x = x
        self.anchor_y = y
        self.cell_size = length // 4

    def redraw_grid(self):
        for x in range(4):
            for y in range(4):
                self.draw_cell(x, y)

    def draw_cell(self, x, y):
        # main_game rect
        s = shapes.Rectangle(x=self.anchor_x - x * self.cell_size,
                             y=self.anchor_y - y * self.cell_size,
                             width=self.cell_size,
                             height=self.cell_size,
                             color=(187, 173, 160))

        s.anchor_x = self.cell_size
        s.anchor_y = self.cell_size
        s.draw()

        self.draw_inner_cell_placeholder(x, y)

    def draw_inner_cell_placeholder(self, x, y):
        # sub rect
        s = shapes.Rectangle(x=self.anchor_x - x * self.cell_size,
                             y=self.anchor_y - y * self.cell_size,
                             width=self.cell_size - 2 * Grid.subRectOffset,
                             height=self.cell_size - 2 * Grid.subRectOffset,
                             color=(205, 193, 180))

        s.anchor_x = self.cell_size - Grid.subRectOffset
        s.anchor_y = self.cell_size - Grid.subRectOffset
        s.draw()

        # str(Game.current.get_block_value(x, y)
        self.draw_text_cell(x, y, str(999999))

    def draw_text_cell(self, x, y, text):
        s = shapes.Rectangle(x=self.anchor_x - x * self.cell_size,
                             y=self.anchor_y - y * self.cell_size,
                             width=self.cell_size - 2 * Grid.subRectOffset,
                             height=self.cell_size - 2 * Grid.subRectOffset,
                             color=(205, 193, 180))

        s.anchor_x = self.cell_size - Grid.subRectOffset
        s.anchor_y = self.cell_size - Grid.subRectOffset
        s.draw()

        pyglet.text.Label(text, font_size=32 - 2 * (len(text)),
                          x=self.anchor_x - x * self.cell_size - self.cell_size // 2,
                          y=self.anchor_y - y * self.cell_size - self.cell_size + self.cell_size // 4,
                          width=self.cell_size - 2 * Grid.subRectOffset,
                          height=self.cell_size - 2 * Grid.subRectOffset,
                          color=(0, 0, 0, 255),
                          anchor_x='center',
                          anchor_y='center').draw()
