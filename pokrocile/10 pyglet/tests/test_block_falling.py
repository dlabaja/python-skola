import pytest

from main_game.game import Game


@pytest.fixture
def game():
    return Game()


def test_move_blocks_down(game):
    game.add_block((0, 1))
    game.add_block((2, 3))

    game.move_blocks_down()

    assert game.map[1][0] is None
    assert game.map[3][0] == game.blocks[0]
    assert game.map[3][2] == game.blocks[1]


def test_move_blocks_down_and_merge(game):
    game.add_block((0, 1))
    game.add_block((0, 2))

    game.move_blocks_down()

    assert game.map[1][0] is None
    assert game.map[2][0] is None
    assert game.map[3][0].value == 4


def test_move_blocks_right(game):
    game.add_block((1, 3))
    game.add_block((3, 1))

    game.move_blocks_right()

    assert game.map[3][1] is None
    assert game.map[3][3] == game.blocks[0]
    assert game.map[1][3] == game.blocks[1]


def test_move_blocks_right_and_merge(game):
    game.add_block((1, 3))
    game.add_block((2, 3))

    game.move_blocks_right()

    assert game.map[3][1] is None
    assert game.map[3][2] is None
    assert game.map[3][3].value == 4
