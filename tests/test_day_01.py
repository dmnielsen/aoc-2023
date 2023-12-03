import pytest

from aoc2023 import day_01 as day


@pytest.fixture
def mock_input():
    return """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


@pytest.fixture
def mock_input_part2():
    return """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_parse_input(mock_input):
    expected = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    result = day.parse_input(mock_input)

    assert all(a == b for a, b in zip(expected, result))


@pytest.mark.parametrize(
    "line,value",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("3asfdtwone", 31),
    ],
)
def test_extract_instructions(line, value):
    result = day.extract_instructions(line)
    assert value == result


def test_solve_part1(mock_input):
    expected = 142
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input_part2):
    expected = 281
    result = day.solve_part2(mock_input_part2)
    assert expected == result
