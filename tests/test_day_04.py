import pytest

from aoc2023 import day_04 as day


@pytest.fixture
def mock_input():
    return """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_parse_card():
    card_text = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

    expected_card_num = 1
    expected_winning_num = {41, 48, 83, 86, 17}
    expected_game_num = {83, 86, 6, 31, 17, 9, 48, 53}

    result_card_num, result_winning_num, result_game_num = day.parse_card(card_text)

    assert expected_card_num == result_card_num
    assert expected_winning_num == result_winning_num
    assert expected_game_num == result_game_num


def test_compare_card_numbers():
    winning_num = {41, 48, 83, 86, 17}
    game_num = {83, 86, 6, 31, 17, 9, 48, 53}

    expected = 4

    result = day.compare_card_numbers(winning_num, game_num)

    assert expected == result


def test_compare_card_numberse_is_zero_with_no_overlap():
    winning_num = {31, 18, 13, 56, 72}
    game_num = {74, 77, 10, 23, 35, 67, 36, 11}

    expected = 0

    result = day.compare_card_numbers(winning_num, game_num)

    assert expected == result


def test_solve_part1(mock_input):
    expected = 13
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 30
    result = day.solve_part2(mock_input)
    assert expected == result
