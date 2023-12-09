import re
from pathlib import Path

import numpy as np

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202309_input.txt"


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> list[np.ndarray]:
    p = re.compile(r"([-\d]+)")
    measurements = []
    for line in text.strip().split("\n"):
        measurements.append(np.array([int(x) for x in p.findall(line)]))
    return measurements


def extrapolate_measurement(numbers: np.ndarray) -> tuple[int, int]:
    diffs = [numbers, np.ediff1d(numbers)]
    while any(diffs[-1]):
        if len(diffs[-1]) == 1:
            breakpoint()
        diffs.append(np.ediff1d(diffs[-1]))

    post_estimate = 0
    pre_estimate = 0
    for diff in reversed(diffs):
        post_estimate += diff[-1]
        pre_estimate = diff[0] - pre_estimate
    return post_estimate, pre_estimate


def solve_both_parts(input_: str) -> tuple[int, int]:
    measurements = parse_input(input_)
    extrapolations = [extrapolate_measurement(measurement) for measurement in measurements]

    pre_estimate = sum(x[0] for x in extrapolations)
    post_estimate = sum(x[1] for x in extrapolations)
    return pre_estimate, post_estimate


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    results = solve_both_parts(input_)
    result1 = results[0]
    result2 = results[1]

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
