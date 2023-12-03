import pytest

from aoc2023 import day_03 as day
from aoc2023.day_03 import Coords


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
    coords = [Coords(x=0, y=5), Coords(x=0, y=6), Coords(x=0, y=7)]
    symbols = {Coords(x=5, y=5), Coords(x=4, y=3), Coords(x=8, y=3), Coords(x=3, y=6), Coords(x=1, y=3), Coords(x=8, y=5)}
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
