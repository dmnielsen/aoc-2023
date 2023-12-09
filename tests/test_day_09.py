import pytest

from aoc2023 import day_09 as day


@pytest.fixture
def mock_input():
    return """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def test_solve_both_parts(mock_input):
    expected = (114, 2)
    result = day.solve_both_parts(mock_input)

    assert expected == result
