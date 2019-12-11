import pytest

from game_of_greed import Game

def test_roll():
    game = Game()
    game_roll = game.roll(6)
    assert max(game_roll) <= 6
    assert min(game_roll) > 0

def test_roll_case2():
    game = Game()
    game_roll = game.roll(2)
    assert max(game_roll) <= 6
    assert min(game_roll) > 0

def test_roll_case1():
    game = Game()
    game_roll = game.roll(1)
    assert max(game_roll) <= 6
    assert min(game_roll) > 0
