import re
from pathlib import Path

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202304_input.txt"


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def extract_card_number(card_text: str) -> int:
    return int(re.findall(r"(\d+)", card_text)[0])


def extract_numbers(text: str) -> set[int]:
    numbers = (int(n) for n in re.findall(r"(\d+)", text))
    return set(numbers)


def parse_card(text: str) -> tuple[int, set[int], set[int]]:
    card_number, numbers = text.strip().split(":")

    winning_numbers, game_numbers = numbers.split(" | ")

    return (
        extract_card_number(card_number),
        extract_numbers(winning_numbers),
        extract_numbers(game_numbers),
    )


def compare_card_numbers(winning_numbers: set[int], game_numbers: set[int]) -> int:
    return len(winning_numbers & game_numbers)


def calculate_card_value(card_text: str) -> int:
    _, winning_nums, game_nums = parse_card(card_text)
    matches = compare_card_numbers(winning_nums, game_nums)
    if not matches:
        return 0
    elif matches == 1:
        return 1
    else:
        return 2 ** (matches - 1)


def process_cards(card_stack, card_tally):
    processed = 0

    while card_stack:
        card = card_stack.pop()
        processed += 1

        matches = card_tally[card]
        if matches:
            card_stack.extend([card + n for n in range(matches, 0, -1)])

    return processed


def solve_part1(input_: str):
    card_values = [calculate_card_value(card) for card in input_.strip().split("\n")]
    return sum(card_values)


def solve_part2(input_: str):
    card_tally = {}
    for card_text in input_.strip().split("\n"):
        num, winning_nums, game_nums = parse_card(card_text)
        card_tally[num] = compare_card_numbers(winning_nums, game_nums)

    cards_to_process = list(reversed(card_tally.keys()))

    return process_cards(cards_to_process, card_tally)

    return


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
