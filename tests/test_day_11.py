import pytest

from aoc2023 import day_11 as day


@pytest.fixture
def mock_input():
    return """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def test_solve_part1(mock_input):
    expected = 374
    result = day.solve_part1(mock_input)
    assert expected == result


@pytest.mark.parametrize("expected,factor", [(374, 2), (1030, 10), (8410, 100)])
def test_solve_part2(mock_input, expected, factor):
    result = day.solve_part2(mock_input, expansion_factor=factor)
    assert expected == result
