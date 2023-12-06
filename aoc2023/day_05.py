from pathlib import Path
from typing import Optional, cast

from aoc2023 import AOC_DIR
from aoc2023.util import print_solutions

INPUT_FILENAME = AOC_DIR / "inputs" / "202305_input.txt"


SeedMap = list[tuple[int, int, int]]
Range = tuple[int, int]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, "r") as f:
        return f.read()


def extract_and_process_map(text: str):
    starts = [tuple(int(n) for n in nums.split(" ")) for nums in text.split("\n")[1:]]
    return starts


def parse_input(text: str) -> tuple[tuple[int, ...], list[SeedMap]]:
    maps = text.strip().split("\n\n")

    seeds = tuple(int(s) for s in maps[0].split(": ")[1].split())

    map_list = []
    for mapping in maps[1:]:
        map_list.append(extract_and_process_map(mapping))
    return seeds, map_list


def map_seed_to_location(seed: int, map_list: list[SeedMap]):
    current_loc = seed

    for mapping in map_list:
        for destination, source, delta in mapping:
            if current_loc in range(source, source + delta):
                current_loc = destination + (current_loc - source)
                break

    return current_loc


def solve_part1(input_: str):
    seeds, maps = parse_input(input_)

    locs = [map_seed_to_location(seed, maps) for seed in seeds]

    return min(locs)


def find_seed_ranges(seed_ranges: tuple[int, ...]):
    pairs = [(start, start + delta - 1) for start, delta in zip(seed_ranges[0::2], cast(tuple[int], seed_ranges[1::2]))]
    return pairs


def backtrack_ranges(ranges: list[tuple[int, int]], mapping):
    backtrack = []

    for start, end in ranges:
        end -= 1

        for curr, prev, delta in sorted(mapping, key=lambda x: x[0]):
            curr_range = range(curr, curr + delta)

            if (start >= curr_range.stop) or (end <= curr_range.start):
                continue

            # destination full contained in source
            if start in curr_range and end in curr_range:
                backtrack.append((prev + (start - curr), prev + (end - curr)))
                continue

            # source fully contained in destination
            if (curr_range.start >= start) and (curr_range.stop < end):
                backtrack.append((prev + curr_range.start - curr, prev + max(curr_range) - curr))
                continue

            # start is enclosed
            if start in curr_range:
                backtrack.append((prev + start - curr, prev + delta))
                continue

            # end is enclosed
            if end in curr_range:
                backtrack.append((prev, prev - end - curr))
                continue

    return backtrack


def range_overlaps(map_range: Range, seed_range: Range) -> bool:
    min_left = min(map_range[0], seed_range[0])
    max_right = max(map_range[1], seed_range[1])

    width1 = map_range[1] - map_range[0]
    width2 = seed_range[1] - seed_range[0]

    return abs(width1 + width2) > (max_right - min_left)


def backtrack_location_mapping(map_list, seed_ranges) -> Optional[int]:
    # Iterate thru each line of the location map until a seed match is found
    for loc, previous, delta in sorted(map_list[-1], key=lambda x: x[0])[:3]:  # Look from small -> large locs
        ranges = [(loc, loc + delta)]

        for map in map_list[-1::-1]:
            ranges = backtrack_ranges(ranges, map)
            pass

        for seed_range in seed_ranges:
            for map_range in ranges:
                if range_overlaps(map_range, seed_range):
                    return max(map_range[0], seed_range[0])

    return None


def solve_part2(input_: str):
    seeds, maps = parse_input(input_)

    seed_ranges = find_seed_ranges(seeds)

    seed_that_maps_to_min = backtrack_location_mapping(maps, seed_ranges)
    assert seed_that_maps_to_min is not None

    return map_seed_to_location(seed_that_maps_to_min, maps)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == "__main__":
    main()
