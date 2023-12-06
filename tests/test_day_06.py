import pytest

from aoc2023 import day_06 as day


@pytest.fixture
def mock_input():
    return """Time:      7  15   30
Distance:  9  40  200"""


def test_parse_input(mock_input):
    expected = [(7, 9), (15, 40), (30, 200)]
    result = day.parse_input(mock_input)

    assert all([e == r for e, r in zip(expected, result)])


def test_parse_input_with_concatenation(mock_input):
    expected = (71530, 940200)
    result = day.parse_input_with_concatenation(mock_input)
    assert expected == result


def calculate_possible_distances():
    expected = [0, 6, 10, 12, 12, 10, 6]

    race_time = 7
    result = day.calculate_possible_distances(race_time)

    assert all([e == r for e, r in zip(expected, result)])


def test_find_min_max_elapsed_time():
    time = 71530
    distance = 940200
    expected = (14, 71516)
    result = day.find_min_max_elapsed_time(time, distance)

    assert expected == result


def test_solve_part1(mock_input):
    expected = 288
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 71503
    result = day.solve_part2(mock_input)
    assert expected == result
