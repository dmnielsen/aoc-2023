import re
from itertools import cycle
from math import lcm
from pathlib import Path
from typing import Callable

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202308_input.txt"


Node = dict[str, str]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> tuple[str, dict[str, Node]]:
    directions, nodes = text.strip().split("\n\n")[:2]

    p = re.compile(r"(\S{3}) = \((\S{3}), (\S{3})\)")
    parse_nodes = p.findall(nodes)
    return directions, {base: {"L": left, "R": right} for base, left, right in parse_nodes}


def found_standard_destination(loc: str) -> bool:
    return loc == "ZZZ"


def found_ghost_destination(loc: str) -> bool:
    return loc[-1] == "Z"


def follow_directions(
    directions: str, nodes: dict[str, Node], start_loc: str = "AAA", found_func: Callable = found_standard_destination
) -> int:
    steps = 0
    current_loc = start_loc

    for i in cycle(directions):
        if found_func(current_loc):
            return steps
        current_loc = nodes[current_loc][i]
        steps += 1

    return -1


def calculate_lcm_of_ghost_directions(directions: str, nodes: dict[str, Node]) -> int:
    starts = [node for node in nodes if node[-1] == "A"]

    steps = [follow_directions(directions, nodes, start, found_ghost_destination) for start in starts]

    return lcm(*steps)


def solve_part1(input_: str):
    directions, nodes = parse_input(input_)

    return follow_directions(directions, nodes)


def solve_part2(input_: str):
    directions, nodes = parse_input(input_)

    return calculate_lcm_of_ghost_directions(directions, nodes)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
