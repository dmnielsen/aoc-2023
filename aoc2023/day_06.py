import re
from math import prod
from pathlib import Path

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202306_input.txt"


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> list[tuple[int, int]]:
    parsed = text.strip().split("\n")

    times = [int(x.group(0)) for x in re.finditer(r"(\d+)", parsed[0])]
    distances = [int(x.group(0)) for x in re.finditer(r"(\d+)", parsed[1])]

    return [(t, d) for t, d in zip(times, distances)]


def parse_input_with_concatenation(text: str) -> tuple[int, int]:
    times, distances = text.strip().split("\n")[:2]

    times = "".join(re.findall(r"(\d+)", times))
    distances = "".join(re.findall(r"(\d+)", distances))

    return int(times), int(distances)


def calculate_possible_distances(time: int) -> list[int]:
    return [(time - charge_time) * charge_time for charge_time in range(time)]


def solve_part1(input_: str):
    records = parse_input(input_)

    ways_to_beat_record = [
        sum([d > distance for d in calculate_possible_distances(time)]) for time, distance in records
    ]
    return prod(ways_to_beat_record)


def find_min_max_elapsed_time(time: int, distance: int) -> tuple[int, int]:
    min_charge_time = -1
    max_charge_time = -1
    for i in range(time):
        if (time - i) * i > distance:
            min_charge_time = i
            break

    for i in range(time, 0, -1):
        if (time - i) * i > distance:
            max_charge_time = i
            break

    return min_charge_time, max_charge_time


def solve_part2(input_: str):
    record = parse_input_with_concatenation(input_)

    min_time, max_time = find_min_max_elapsed_time(*record)

    return max_time - min_time + 1


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
