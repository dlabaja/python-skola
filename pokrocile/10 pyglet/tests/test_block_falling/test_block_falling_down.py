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


def test_multimerge(game):
    game.add_block((0, 0))
    game.add_block((0, 1))
    game.add_block((0, 2))
    game.add_block((0, 3))

    game.blocks[0].value = 32
    game.blocks[1].value = 16
    game.blocks[2].value = 8
    game.blocks[3].value = 8

    game.move_blocks_down()

    assert game.map[3][0].value == 64
