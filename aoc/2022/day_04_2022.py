from dataclasses import dataclass
from re import findall
from typing import Any
from aoc import utils


GroupPairSetType = list[list[set[int]]]


@dataclass
class ReturnType:
    group_matches: int
    overlapping_matches: int


def setup() -> GroupPairSetType:
    group_pairs: GroupPairSetType = []
    for group in inputdata:
        elf_one_start, elf_one_end, elf_two_start, elf_two_end = list(
            map(int, findall("[0-9]+", group))
        )
        group_pairs.append([set(range(elf_one_start, elf_one_end + 1)),
                            set(range(elf_two_start, elf_two_end + 1))])
    return group_pairs


def get_matches() -> ReturnType:
    data = setup()
    group_matches: int = 0
    overlapping_matches: int = 0

    for group_one, group_two in data:
        if any([group_two.issubset(group_one), group_one.issubset(group_two)]):
            group_matches += 1

        if group_one.intersection(group_two):
            overlapping_matches += 1

    return ReturnType(
        group_matches=group_matches,
        overlapping_matches=overlapping_matches
    )


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return get_matches().group_matches


@utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return get_matches().overlapping_matches


# Fixed test data
inputdata = utils.get_day_data(4, test_data=True)
assert part1(silent=True) == 2  # type: ignore
assert part2(silent=True) == 4  # type: ignore

inputdata = utils.get_day_data(4, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
