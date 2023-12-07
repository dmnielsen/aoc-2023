import pytest

from aoc2023 import day_07 as day


@pytest.fixture
def mock_input():
    return """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def test_solve_part1(mock_input):
    expected = 6440
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 5905
    result = day.solve_part2(mock_input)
    assert expected == result
