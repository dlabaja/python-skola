import pyglet
from pyglet import shapes
from main_game.game import Game

class Grid:
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
        r = shapes.Rectangle(x=self.anchor_x - x * self.cell_size, y=self.anchor_y - y * self.cell_size,
                             width=self.cell_size, height=self.cell_size,
                             color=(255, 255, 255))
        r.anchor_x = self.cell_size
        r.anchor_y = self.cell_size
        r.draw()

        # sub rect
        sr = shapes.Rectangle(x=self.anchor_x - x * self.cell_size, y=self.anchor_y - y * self.cell_size,
                             width=self.cell_size * 0.8, height=self.cell_size * 0.8,
                             color=(55, 55, 255))
        sr.anchor_x = self.cell_size * 0.8
        sr.anchor_y = self.cell_size * 0.8
        sr.draw()

        label = pyglet.text.Label(str(Game.current.get_block_value(x, y)), font_size=20,
                                  x=self.anchor_x - self.cell_size // 2,  # Center horizontally
                                  y=self.anchor_y - self.cell_size // 2)  # Center vertically
        label.draw()
