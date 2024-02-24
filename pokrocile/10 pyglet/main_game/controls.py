from pyglet.window import key
from main_game.game import Game


class Controls:
    keys = key.KeyStateHandler()

    @staticmethod
    def on_key_press(symbol, _):
        if Game.current.ended:
            return

        if symbol == key.W or symbol == key.UP:
            if Game.current.move_blocks_up():
                Game.current.next_turn()
        elif symbol == key.A or symbol == key.LEFT:
            if Game.current.move_blocks_left():
                Game.current.next_turn()
        elif symbol == key.S or symbol == key.DOWN:
            if Game.current.move_blocks_down():
                Game.current.next_turn()
        elif symbol == key.D or symbol == key.RIGHT:
            if Game.current.move_blocks_right():
                Game.current.next_turn()
