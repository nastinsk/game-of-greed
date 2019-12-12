import pytest

from game_of_greed import Game

def test_Game_instance():
    game = Game()
    assert game

def test_zilch():
    my_game = Game()
    assert my_game.calculate_score((2, 3, 4, 6, 6, 3)) == 0

# this test also checks for the cases described in test_leftover_ones
@pytest.mark.parametrize("test_input,expected", [((1, 1, 1, 1, 1, 1), 4000), ((1, 1, 1, 1, 1, 2), 3000), ((1, 1, 1, 1, 3, 2), 2000), ((1, 1, 1, 3, 2, 4), 1000), ((1, 1, 3, 3, 2, 4), 200),((1, 2, 3, 3, 2, 4), 100)])
def test_ones(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [((2, 2, 2, 2, 2, 2), 800), ((2, 2, 2, 2, 2, 3), 600), ((2, 2, 2, 2, 3, 4), 400), ((2, 2, 2, 3, 6, 4), 200)])
def test_twos(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [((3,3,3,3,3,3), 1200), ((3, 2, 3, 3, 3, 3), 900), ((3, 2, 3, 3, 3, 4), 600), ((2, 3, 3, 3, 6, 4), 300)])
def test_threes(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [((4,4,4,4,4,4), 1600), ((3, 4, 4, 4, 4, 4), 1200), ((4, 2, 4, 4, 3, 4), 800), ((2, 4, 4, 3, 6, 4), 400)])
def test_fours(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected

# this test also checks for the cases described in test_leftover_fives
@pytest.mark.parametrize("test_input,expected", [((5,5,5,5,5,5), 2000), ((5, 5, 4, 5, 5, 5), 1500), ((4, 5, 5, 4, 5, 5), 1000), ((5, 4, 5, 5, 6, 4), 500), ((5, 6, 5, 2, 3, 4), 100), ((5, 4, 2, 3, 6, 4), 50)])
def test_fives(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [((6,6,6,6,6,6), 2400), ((4, 6, 6, 6, 6, 6), 1800), ((6, 6, 6, 4, 6, 2), 1200), ((6, 4, 6, 2, 6, 4), 600)])
def test_sixes(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [((1, 2, 3, 4, 5, 6), 1500), ((4, 6, 1, 3, 2, 5), 1500), ((1, 2, 3, 4, 5, 9), 'invalid value')])
def test_straight(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [((1, 1, 2, 2, 3, 3), 1500), ((4, 6, 5, 6, 4, 5), 1500), ((1, 1, 1, 1, 5, 5), 2100),  ((2, 2, 2, 2, 4, 4), 400)])
def test_three_unique_pairs(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [((3, 3, 3, 5, 5, 5), 800), ((4, 4, 4, 1, 1, 1), 1400), ((1, 1, 1, 5, 5, 5), 1500),  ((2, 2, 2, 3, 3, 3), 500)])
def test_two_trios(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [((5, 1, 1, 5, 5, 5), 2000), ((5, 5, 5, 5, 1, 1), 2000), ((1, 1, 5, 5, 5, 5), 2000)])
def test_mcflurry(test_input, expected):
    my_game = Game()
    assert my_game.calculate_score(test_input) == expected
