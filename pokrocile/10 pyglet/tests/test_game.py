import pytest

from main_game.game import Game


@pytest.fixture
def game():
    return Game()


def test_remove_block(game):
    game.add_block([0, 0])
    game.add_block([0, 1])

    assert len(game.blocks) == 2
    game.remove_block(game.blocks[1])
    assert len(game.blocks) == 1


def test_merge_blocks(game):
    game.add_block([0, 0])
    game.add_block([0, 1])

    assert len(game.blocks) == 2
    game.merge_blocks(game.blocks[0], game.blocks[1])

    assert len(game.blocks) == 1
    assert game.blocks[0].value == 4
    assert game.blocks[0].pos == [0, 0]

    assert game.map[1][0] is None
    assert game.map[0][0].value == 4


def test_add_block(game):
    assert len(game.blocks) == 0
    game.add_block([0, 0])

    assert len(game.blocks) == 1

    assert game.blocks[0].pos == [0, 0]
    assert game.blocks[0].value == 2

    assert game.map[0][0] == game.blocks[0]


def test_add_block_with_same_coords(game):
    game.add_block([0, 0])
    game.add_block([0, 0])

    assert len(game.blocks) == 1
    assert game.blocks[0].value == 4

    assert game.map[0][0].value == 4


def test_get_free_cells(game):
    game.add_block([0, 0])
    assert len(game.get_free_cells()) == 4 * 4

    game.add_block([0, 0])
    assert len(game.get_free_cells()) == 4 * 4 - 1


def test_end(game):
    for y in range(4):
        for x in range(4):
            game.add_block([x, y])
            game.add_block([x, y])

    game.next_turn()
    assert game.ended is True
