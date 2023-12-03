import re
from pathlib import Path

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202301_input.txt"

INSTRUCTION_PATTERN = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

CONVERT_NUMBERS = {
    word: i for i, word in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], start=1)
}


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> list[str]:
    return text.split("\n")


def extract_instructions(text: str, p: re.Pattern[str] = INSTRUCTION_PATTERN) -> int:
    match = p.findall(text)
    if match:
        first = CONVERT_NUMBERS.get(match[0], match[0])
        last = CONVERT_NUMBERS.get(match[-1], match[-1])

        return int(f"{first}{last}")
    else:
        print(text)
        return 0


def solve_part1(input_: str) -> int:
    instructions = parse_input(input_)

    pattern = re.compile(r"\d")

    return sum(extract_instructions(line, pattern) for line in instructions)


def solve_part2(input_: str) -> int:
    instructions = parse_input(input_)

    calibration_values = [extract_instructions(line) for line in instructions]

    return sum(calibration_values)


def main(show_solution: bool = True) -> None:
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
