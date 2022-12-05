from typing import Any
import numpy as np
from aoc import utils


def setup() -> tuple[list[Any], list[str]]:
    diagram = inputdata[0].split("\n")
    move_instructions = inputdata[1].split("\n")
    stacks = []
    for row in diagram[:-1]:
        stacks += [[*row[1:len(diagram[0]):4]]]

    ret = ([
        list(filter(lambda x: x != " ", lst)) for lst in np.array(stacks).T.tolist()
    ], move_instructions)

    return ret


def solve(upgraded: bool = False) -> str:
    stacks, move_instructions = setup()
    for instruction in move_instructions:
        try:
            move_amount, move_from, move_to = map(int, instruction.split(" ")[1::2])
            if upgraded:
                items_to_move = stacks[move_from-1][:move_amount]
            else:
                items_to_move = stacks[move_from-1][:move_amount][::-1]
            stacks[move_to-1] = items_to_move + stacks[move_to-1]
            stacks[move_from-1] = stacks[move_from-1][move_amount:]
        except ValueError:
            continue

    return "".join([x[0] for x in stacks])


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> str:  # pylint: disable=unused-argument
    return solve()


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> str:  # pylint: disable=unused-argument
    return solve(upgraded=True)


day_func_arguments = {"no_strip": True, "split_delimiter": "\n\n"}
# Fixed test data
inputdata = utils.get_day_data(
    5, test_data=True, **day_func_arguments)
assert part1(silent=True) == "CMZ"  # type: ignore
assert part2(silent=True) == "MCD"  # type: ignore

inputdata = utils.get_day_data(
    5, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
