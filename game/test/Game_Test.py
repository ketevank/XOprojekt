import pytest
from game.Game import *

def test_cokolwiek():
    game = Game()
    assert game.players[0].sign == 'X'
    assert game.players[1].sign == 'O'

    assert game.players[0].sign != game.players[1].sign

def test_mark_field():
    game = Game()
    player = game.players[0]
    player.mark_field(3, 1)
    assert player.marked_fields[0].x == 3
    assert player.marked_fields[0].y == 1

