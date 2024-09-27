from pyglet.window import key
from main_game.game import Game


class Controls:
    keys = key.KeyStateHandler()

    @staticmethod
    def key_mapping():
        return {
            (key.W, key.UP): Game.current.move_blocks_up,
            (key.A, key.LEFT): Game.current.move_blocks_left,
            (key.S, key.DOWN): Game.current.move_blocks_down,
            (key.D, key.RIGHT): Game.current.move_blocks_right,
            key.P: Controls.reset_game()
        }

    @staticmethod
    def reset_game():
        Game.current = Game

    @staticmethod
    def on_key_press(symbol, _):
        for key_pair, movement_function in Controls.key_mapping().items():
            if symbol in key_pair:
                if movement_function():
                    Game.current.next_turn()
                break
