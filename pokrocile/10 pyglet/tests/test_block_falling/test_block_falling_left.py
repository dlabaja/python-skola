import pytest

from main_game.game import Game


@pytest.fixture
def game():
    return Game()


def test_move_blocks_left(game):
    game.add_block((2, 0))
    game.add_block((0, 2))

    game.move_blocks_left()

    assert game.map[0][2] is None
    assert game.map[2][0] == game.blocks[1]
    assert game.map[0][0] == game.blocks[0]
