from pathlib import Path
from typing import NamedTuple

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202302_input.txt"


class Handful(NamedTuple):
    blue: int = 0
    green: int = 0
    red: int = 0


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> list[str]:
    return text.split("\n")


def parse_handful(text: str) -> Handful:
    cubes = text.split(", ")
    return Handful(**{cube.split()[1]: int(cube.split()[0]) for cube in cubes})


def parse_game(text: str) -> tuple[int, list[Handful]]:
    game_number, cubes = text.split(":")
    number = int(game_number.split()[-1])

    subsets = cubes.strip().split(";")
    return number, [parse_handful(subset) for subset in subsets]


def is_impossible(handful: Handful, compare: Handful) -> bool:
    return (handful.red > compare.red) or (handful.blue > compare.blue) or (handful.green > compare.green)


def check_if_game_is_impossible(text: str, comparison_handful: Handful) -> int:
    number, subsets = parse_game(text)

    if any(is_impossible(subset, comparison_handful) for subset in subsets):
        return 0
    else:
        return number


def solve_part1(input_: str) -> int:
    games = parse_input(input_.strip())

    comparison_handful = Handful(red=12, green=13, blue=14)
    return sum(check_if_game_is_impossible(game, comparison_handful) for game in games)


def calculated_power_of_cube_set(text: str) -> int:
    _, subsets = parse_game(text)

    red = max(subset.red for subset in subsets)
    green = max(subset.green for subset in subsets)
    blue = max(subset.blue for subset in subsets)

    return red * green * blue


def solve_part2(input_: str) -> int:
    games = parse_input(input_.strip())

    return sum(calculated_power_of_cube_set(game) for game in games)


def main(show_solution: bool = True) -> None:
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
