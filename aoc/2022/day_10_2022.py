from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from aoc import utils


SIGNAL_STRENGTH_DURING = list(range(20, 220+1, 40))


class Operation(int, Enum):
    noop = 1
    addx = 2


@dataclass
class Instruction:
    operation: Operation
    amount: int
    cycles_remaining: int = field(init=False)

    def __post_init__(self) -> None:
        self.cycles_remaining = self.operation.value


class Solver:
    def __init__(self) -> None:
        self.cycle_number: int = 0
        self.x_register: int = 1
        self.signal_strengths = {x: 0 for x in SIGNAL_STRENGTH_DURING}

    def run(self) -> None:
        for line in inputdata:
            line_split = line.split(" ")
            if len(line_split):
                line_split.append("0")
            current_instruction = Instruction(
                Operation[line_split[0]], int(line_split[1]))

            while current_instruction.cycles_remaining > 0 and self.cycle_number <= 220:
                self.cycle_number += 1
                if self.cycle_number in SIGNAL_STRENGTH_DURING:
                    self.signal_strengths[self.cycle_number] = self.cycle_number * \
                        self.x_register
                current_instruction.cycles_remaining -= 1

            if current_instruction.operation.name == "noop":
                continue

            if self.cycle_number in SIGNAL_STRENGTH_DURING:
                self.signal_strengths[self.cycle_number] = self.cycle_number * \
                    self.x_register

            if self.cycle_number == SIGNAL_STRENGTH_DURING[-1]:
                break

            self.x_register += current_instruction.amount

    def get_total_signal_strength(self) -> int:
        self.run()
        return sum(self.signal_strengths.values())


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return Solver().get_total_signal_strength()


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return 0


# Fixed test data
inputdata = utils.get_day_data(10, test_data=True)
assert part1(silent=True) == 13140  # type: ignore
assert part2(silent=True) == 0  # type: ignore

inputdata = utils.get_day_data(10, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
