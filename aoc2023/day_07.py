import re
from collections import Counter
from pathlib import Path

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202307_input.txt"


class Card:
    def __init__(self, label: str):
        self.label = label
        self.rank = self.assign_rank()

    def __repr__(self) -> str:
        return f"Card({self.label})"

    def assign_rank(self) -> int:
        try:
            n = int(self.label)
            if 1 < n < 10:
                return n
            else:
                raise ValueError("Numeric value must be an integer 2 to 9")
        except ValueError:
            return {
                "T": 10,
                "J": 11,
                "Q": 12,
                "K": 13,
                "A": 14,
                "W": 0,
            }[self.label]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.label == other.label

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank > other.rank

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return not self.__gt__(other)


class Hand:
    def __init__(self, hand: str) -> None:
        self.raw_hand = hand
        self.hand = Counter(hand)
        self.cards = [Card(s) for s in hand]
        self.value = self.assign_hand_value()

    def __repr__(self) -> str:
        return f"Hand({''.join(self.raw_hand)})"

    def assign_hand_value(self) -> int:
        hand_types = {
            self.is_five_of_a_kind: 6,
            self.is_four_of_a_kind: 5,
            self.is_full_house: 4,
            self.is_three_of_a_kind: 3,
            self.is_two_pair: 2,
            self.is_one_pair: 1,
        }
        for func, value in hand_types.items():
            if func():
                return value
        return 0

    def is_five_of_a_kind(self) -> bool:
        return len(self.hand) == 1

    def is_four_of_a_kind(self) -> bool:
        return max(self.hand.values()) == 4

    def is_full_house(self) -> bool:
        return (max(self.hand.values()) == 3) and (min(self.hand.values()) == 2)

    def is_three_of_a_kind(self) -> bool:
        return (len(self.hand) == 3) and (max(self.hand.values()) == 3)

    def is_two_pair(self) -> bool:
        return (len(self.hand) == 3) and (max(self.hand.values()) == 2)

    def is_one_pair(self) -> bool:
        return len(self.hand) == 4

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        breakpoint()
        return self.value == other.value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        if self.value > other.value:
            return True
        elif self.value == other.value:
            for this, compare in zip(self.cards, other.cards):
                if this > compare:
                    return True
                elif compare > this:
                    return False
        return False

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__gt__(other)


class HandWildJacks(Hand):
    def __init__(self, hand: str) -> None:
        super().__init__(hand)
        self.cards = [Card(c) for c in hand.replace("J", "W")]

    def __repr__(self) -> str:
        return f"HandWildJacks('{self.raw_hand}')"

    def assign_hand_value(self) -> int:
        if num_jacks := self.hand.get("J", 0):
            if num_jacks == 5:
                return 6
            del self.hand["J"]
            most_common_strength, _ = self.hand.most_common()[0]
            self.hand.update({most_common_strength: num_jacks})
        return super().assign_hand_value()


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def parse_input(text: str) -> list[tuple[str, str]]:
    p = re.compile(r"(\S{5}) (\d+)\n")
    return p.findall(text)


def sort_hands(hands_and_bids, hand_type=Hand) -> list[tuple[Hand, int]]:
    hands = [(hand_type(hand), int(bid)) for hand, bid in hands_and_bids]
    return sorted(hands, key=lambda x: x[0])


def total_hands(sorted_hands: list[tuple[Hand, int]]) -> int:
    return sum([i * hand[1] for i, hand in enumerate(sorted_hands, start=1)])


def solve_part1(input_: str) -> int:
    parsed = parse_input(input_)
    sorted_hands = sort_hands(parsed)
    return total_hands(sorted_hands)


def solve_part2(input_: str) -> int:
    parsed = parse_input(input_)
    sorted_hands = sort_hands(parsed, HandWildJacks)
    return total_hands(sorted_hands)


def main(show_solution: bool = True) -> None:
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
