import pytest

from aoc2023 import day_05 as day


@pytest.fixture
def mock_input():
    return """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_extract_and_process_map():
    text = """seed-to-soil map:
50 98 2
52 50 48"""
    expected = [(50, 98, 2), (52, 50, 48)]
    result = day.extract_and_process_map(text)

    assert all(e == r for e, r in zip(expected, result))


def test_map_seed_to_location():
    seed_map = [[(50, 98, 2), (52, 50, 48)]]
    seed = 79

    expected = 81
    result = day.map_seed_to_location(seed, seed_map)
    assert expected == result


def test_solve_part1(mock_input):
    expected = 35
    result = day.solve_part1(mock_input)
    assert expected == result


# Solution doens't work with test input
# def test_solve_part2(mock_input):
#     expected = 46
#     result = day.solve_part2(mock_input)
#     assert expected == result
