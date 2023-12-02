import pytest

from aoc2023 import day_02 as day


@pytest.fixture
def mock_input():
    return """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_parse_handful():
    sample = '1 red, 2 green, 6 blue'
    expected = day.Handful(**{'blue': 6, 'red': 1, 'green': 2})
    result = day.parse_handful(sample)
    assert expected == result


def test_parse_game():
    text = 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'
    expected_number = 2
    expected_samples = [day.Handful(blue=1, green=2), day.Handful(green=3, blue=4, red=1), day.Handful(blue=1, green=1)]

    result_number, result_handful = day.parse_game(text)
    assert expected_number == result_number
    assert all(expected == result for expected, result in zip(expected_samples, result_handful))


def test_check_if_game_is_impossible_returns_zero_if_impossible():
    expected = 0
    text = 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'
    comparison_handful = day.Handful(red=12, green=13, blue=14)

    result = day.check_if_game_is_impossible(text, comparison_handful)
    assert expected == result


def test_check_if_game_is_impossible_return_game_number_if_possible():
    expected = 5

    comparison_handful = day.Handful(red=12, green=13, blue=14)
    text = 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    result = day.check_if_game_is_impossible(text, comparison_handful)
    assert expected == result


def test_calculated_power_of_cube_set():
    expected = 1560
    text = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'

    result = day.calculated_power_of_cube_set(text)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 8
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 2286
    result = day.solve_part2(mock_input)
    assert expected == result
