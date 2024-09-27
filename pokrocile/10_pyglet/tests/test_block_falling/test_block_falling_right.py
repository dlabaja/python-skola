import pytest

from main_game.game import Game


@pytest.fixture
def game():
    return Game()


def test_move_blocks_right(game):
    game.add_block((1, 3))
    game.add_block((3, 1))

    game.move_blocks_right()

    assert game.map[3][1] is None
    assert game.map[3][3] == game.blocks[0]
    assert game.map[1][3] == game.blocks[1]


def test_merge_blocks_from_top(game):
    game.add_block((1, 3))
    game.add_block((2, 3))

    game.move_blocks_right()

    assert game.map[3][1] is None
    assert game.map[3][2] is None
    assert game.map[3][3].value == 4


def test_merge_blocks_from_right(game):
    game.add_block((0, 3))
    game.add_block((3, 3))

    game.move_blocks_right()

    assert game.map[3][0] is None
    assert game.map[3][3].value == 4
