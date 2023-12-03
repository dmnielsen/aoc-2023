import pytest

from aoc2023 import day_03 as day


@pytest.fixture
def mock_input():
    return """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_number_is_adjacent_to_symbol():
    expected = False
    coords = [(0, 5), (0, 6), (0, 7)]
    symbols = {(5, 5), (4, 3), (8, 3), (3, 6), (1, 3), (8, 5)}
    result = day.number_is_adjacent_to_symbol(coords, symbols)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 4361
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 467835
    result = day.solve_part2(mock_input)
    assert expected == result
