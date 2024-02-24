import threading

from gui.renderer import Renderer
from main_game.game import Game


def init_renderer():
    Renderer.initialize(width=800, height=600, title="Pyglet Application")


if __name__ == "__main__":
    game = Game()

    r_thread = threading.Thread(target=init_renderer)
    r_thread.start()

    game.next_turn()
    game.next_turn()
