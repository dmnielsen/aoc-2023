from itertools import combinations
from pathlib import Path

import numpy as np

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202311_input.txt"


Point = tuple[int, int]
Grid = np.ndarray


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> Grid:
    lines = text.strip().split("\n")
    return np.array([list(line) for line in lines])


def expand_space(grid: Grid, empty_marker: str) -> Grid:
    grid = grid.copy()

    # expand columns first
    empty_cols = []
    empty_rows = []

    for col in range(grid.shape[1]):
        if all(grid[:, col] == empty_marker):
            empty_cols.append(col)

    for row in range(grid.shape[0]):
        if all(grid[row, :] == empty_marker):
            empty_rows.append(row)

    for col in reversed(empty_cols):
        grid = np.insert(grid, col, ".", axis=1)

    for row in reversed(empty_rows):
        grid = np.insert(grid, row, ".", axis=0)

    return grid


def calculate_manhattan_distance(first: Point, second: Point) -> int:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def calculate_manhattan_distance_with_expansion(
    grid: Grid, point1: Point, point2: Point, replacement_value: int
) -> int:
    row_range = min(point1[0], point2[0]), max(point1[0], point2[0])
    col_range = min(point1[1], point2[1]), max(point1[1], point2[1])

    extract_row = grid[row_range[0], col_range[0] : col_range[1]].copy()
    extract_col = grid[row_range[0] + 1 : row_range[1] + 1, col_range[0]].copy()

    extract_row[extract_row == "#"] = 1
    extract_col[extract_col == "#"] = 1

    return sum([int(v) if (v == "1" or v == "#") else replacement_value for v in extract_col]) + sum(
        [int(v) if (v == "1" or v == "#") else replacement_value for v in extract_row]
    )


def get_galaxy_coords(grid: Grid) -> list[tuple[int, int]]:
    rows, cols = np.where(grid == "#")
    return [(row, col) for row, col in zip(rows, cols)]


def solve_part1(input_: str):
    grid = parse_input(input_)

    expanded_grid = expand_space(grid, ".")

    galaxy_coords = get_galaxy_coords(expanded_grid)

    return sum([calculate_manhattan_distance(*combos) for combos in combinations(galaxy_coords, 2)])


def parse_input_part2(text: str) -> Grid:
    lines = text.strip().split("\n")
    return np.array([list(line.replace(".", "1")) for line in lines])


def really_expand_space(grid: Grid) -> Grid:
    grid = grid.copy()

    # expand columns first
    empty_cols = []
    empty_rows = []

    for col in range(grid.shape[1]):
        if all(grid[col, :] == "1"):
            empty_cols.append(col)

    for row in range(grid.shape[0]):
        if all(grid[:, row] == "1"):
            empty_rows.append(row)

    for col in reversed(empty_cols):
        grid = np.insert(grid, col, "R", axis=0)
        grid = np.delete(grid, col + 1, axis=0)

    for row in reversed(empty_rows):
        grid = np.insert(grid, row, "R", axis=1)
        grid = np.delete(grid, row + 1, axis=1)

    return grid


def solve_part2(input_: str, expansion_factor: int = 1000000):
    grid = parse_input_part2(input_)
    expanded_grid = really_expand_space(grid)
    galaxy_coords = get_galaxy_coords(expanded_grid)

    return sum(
        [
            calculate_manhattan_distance_with_expansion(expanded_grid, *combos, replacement_value=expansion_factor)
            for combos in combinations(galaxy_coords, 2)
        ]
    )


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
