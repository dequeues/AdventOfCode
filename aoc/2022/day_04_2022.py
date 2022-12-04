from re import findall
from typing import Any
from aoc import utils

GroupPairSetType = list[list[set[int]]]


def setup() -> GroupPairSetType:
    group_pairs: GroupPairSetType = []
    for group in inputdata:
        elf_one_start, elf_one_end, elf_two_start, elf_two_end = list(
            map(int, findall("[0-9]+", group))
        )
        group_pairs.append([set(range(elf_one_start, elf_one_end + 1)),
                            set(range(elf_two_start, elf_two_end + 1))])
    return group_pairs


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    data = setup()
    group_matches: int = 0

    for group_one, group_two in data:
        if any([group_two.issubset(group_one), group_one.issubset(group_two)]):
            group_matches += 1

    return group_matches


@utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return 0


# Fixed test data
inputdata = utils.get_day_data(4, test_data=True)
assert part1(silent=True) == 2  # type: ignore
assert part2(silent=True) == 0  # type: ignore

inputdata = utils.get_day_data(4, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
