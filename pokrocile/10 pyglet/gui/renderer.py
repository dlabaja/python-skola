import pyglet
from pyglet import shapes, gl

from gui.grid import Grid


class Renderer:
    grid = None
    window = None
    x_offset = 25
    y_offset = 25
    menu_width = 200

    @staticmethod
    def initialize(width, height, title):
        r = Renderer

        r.window = pyglet.window.Window(width=width, height=height, caption=title)
        r.window.on_draw = r.on_draw
        r.window.set_minimum_size(800, 600)

        size = r.calculate_grid_size()
        r.grid = Grid(size, r.window.width - r.x_offset, r.window.height - r.y_offset)

        pyglet.app.run()

    @staticmethod
    def on_draw():
        Renderer.window.clear()
        Renderer.draw_window()
        Renderer.grid.redraw_grid()

    @staticmethod
    def draw_window():
        shapes.Rectangle(x=0,
                         y=0,
                         width=Renderer.window.width,
                         height=Renderer.window.width,
                         color=(250, 248, 239)).draw()

    @staticmethod
    def calculate_grid_size():
        shortest = min(Renderer.window.width - Renderer.menu_width - 2 * Renderer.x_offset,
                       Renderer.window.height - 2 * Renderer.y_offset)
        return shortest
