import pytest

from aoc2023 import day_08 as day


@pytest.fixture
def mock_input():
    return """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""


@pytest.fixture
def mock_input2():
    return """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""


def test_parse_input(mock_input):
    expected = (
        "RL",
        {
            "AAA": {"L": "BBB", "R": "CCC"},
            "BBB": {"L": "DDD", "R": "EEE"},
            "CCC": {"L": "ZZZ", "R": "GGG"},
            "DDD": {"L": "DDD", "R": "DDD"},
            "EEE": {"L": "EEE", "R": "EEE"},
            "GGG": {"L": "GGG", "R": "GGG"},
            "ZZZ": {"L": "ZZZ", "R": "ZZZ"},
        },
    )
    result = day.parse_input(mock_input)
    assert expected == result


def test_follow_directions():
    directions, nodes = (
        "RL",
        {
            "AAA": {"L": "BBB", "R": "CCC"},
            "BBB": {"L": "DDD", "R": "EEE"},
            "CCC": {"L": "ZZZ", "R": "GGG"},
            "DDD": {"L": "DDD", "R": "DDD"},
            "EEE": {"L": "EEE", "R": "EEE"},
            "GGG": {"L": "GGG", "R": "GGG"},
            "ZZZ": {"L": "ZZZ", "R": "ZZZ"},
        },
    )

    expected = 2
    result = day.follow_directions(directions, nodes)

    assert expected == result


def test_solve_part1(mock_input):
    expected = 2
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part1_second_mock(mock_input2):
    expected = 6
    result = day.solve_part1(mock_input2)
    assert expected == result


@pytest.fixture
def mock_input_ghost():
    return """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def test_solve_part2(mock_input_ghost):
    expected = 6
    result = day.solve_part2(mock_input_ghost)
    assert expected == result
