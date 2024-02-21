import pytest

from game.game import Game


@pytest.fixture
def game():
    return Game()


def test_merge_blocks(game):
    game.add_block([0, 0])
    game.add_block([0, 1])

    assert len(game.blocks) == 2
    game.merge_blocks(game.blocks[0], game.blocks[1])

    assert len(game.blocks) == 1
    assert game.blocks[0].value == 4
    assert game.blocks[0].pos == [0, 0]


def test_add_block(game):
    assert len(game.blocks) == 0
    game.add_block([0, 0])

    assert len(game.blocks) == 1

    assert game.blocks[0].pos == [0, 0]
    assert game.blocks[0].value == 2
