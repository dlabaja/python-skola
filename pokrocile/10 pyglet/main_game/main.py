import threading

from gui.renderer import Renderer
from main_game.game import Game


def init_renderer():
    Renderer.initialize(width=800, height=600, title="Dva tisíce čtyřicet osm")


if __name__ == "__main__":
    game = Game()

    r_thread = threading.Thread(target=init_renderer)
    r_thread.start()

    game.next_turn()
    game.next_turn()

    #for x in range(4):
    #    for y in range(4):
    #        game.add_block((x, y), 4)

