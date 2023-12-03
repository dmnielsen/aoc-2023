from pathlib import Path
from collections import defaultdict

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202303_input.txt"


Coords = tuple[int, int]
Part = tuple[list[Coords], int]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> tuple[list[Part], set[Coords], set[Coords]]:
    numbers: list[tuple] = []
    symbols = set()
    gears = set()

    for x, line in enumerate(text.strip().split("\n")):
        current_number, current_number_coords = "", []
        for y, point in enumerate(line):
            if point.isnumeric():
                current_number += point
                current_number_coords.append((x, y))
            else:
                if current_number:
                    numbers.append((current_number_coords, int(current_number)))
                    current_number, current_number_coords = "", []

                if point != ".":
                    symbols.update([(x, y)])
                if point == "*":
                    gears.update([(x, y)])

        if current_number:
            numbers.append((current_number_coords, int(current_number)))

    return numbers, symbols, gears


def get_adjacent_coords(point: Coords) -> set[Coords]:
    x, y = point

    adj_points = set((xx, yy) for xx in [x - 1, x, x + 1] for yy in [y - 1, y, y + 1])
    adj_points.remove(point)
    return adj_points


def number_is_adjacent_to_symbol(points: list[Coords], symbols: set[Coords]) -> bool:
    for coord in points:
        for adj_point in get_adjacent_coords(coord):
            if adj_point in symbols:
                return True
    return False


def find_adjacent_gear(points: list[Coords], gears: set[Coords]) -> set[Coords]:
    adj_gears = set()
    for coord in points:
        for adj_point in get_adjacent_coords(coord):
            if adj_point in gears:
                adj_gears.update([adj_point])
    return adj_gears


def find_gears(parts: list[Part], symbols: set[Coords], gears: set[Coords]) -> dict[Coords, list[int]]:
    gears_with_adj_parts = defaultdict(list)
    for coords, value in parts:
        if number_is_adjacent_to_symbol(coords, symbols):
            if adj_gears := find_adjacent_gear(coords, gears):
                for gear in adj_gears:
                    gears_with_adj_parts[gear].append(value)
    return gears_with_adj_parts


def solve_part1(input_: str) -> int:
    numbers, symbols, _ = parse_input(input_)

    part_number_sum = 0
    for coords, value in numbers:
        if number_is_adjacent_to_symbol(coords, symbols):
            part_number_sum += value
    return part_number_sum


def solve_part2(input_: str) -> int:
    numbers, symbols, gears = parse_input(input_)
    possible_gears = find_gears(numbers, symbols, gears)

    gear_ratios = [value[0] * value[1] for value in possible_gears.values() if len(value) == 2]

    return sum(gear_ratios)


def main(show_solution: bool = True) -> None:
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions.print_solutions(result1, result2)


if __name__ == "__main__":
    main()
