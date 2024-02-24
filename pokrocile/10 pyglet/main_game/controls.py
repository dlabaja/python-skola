from pyglet.window import key
from main_game.game import Game


class Controls:
    keys = key.KeyStateHandler()

    @staticmethod
    def on_key_press(symbol, _):
        if symbol == key.W or symbol == key.UP:
            print("Key W or UP Arrow pressed")
        elif symbol == key.A or symbol == key.LEFT:
            print("Key A or LEFT Arrow pressed")
        elif symbol == key.S or symbol == key.DOWN:
            if Game.current.move_blocks_down():
                Game.current.next_turn()
        elif symbol == key.D or symbol == key.RIGHT:
            print("Key D or RIGHT Arrow pressed")
