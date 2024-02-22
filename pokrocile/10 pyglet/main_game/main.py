from gui.renderer import Renderer
from main_game.game import Game

if __name__ == "__main__":
    game = Game()
    renderer = Renderer.initialize(width=800, height=600, title="Pyglet Application")
