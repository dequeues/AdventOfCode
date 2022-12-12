from dataclasses import dataclass
from math import prod
from typing import Any, Callable, Literal, Union

import numpy as np

from aoc import utils

MATH_OPERATORS: dict[str, Callable[[int, int], int]] = {
    "*": np.multiply,
    "+": np.add,
}


@ dataclass
class Test:
    divisible_by: int
    test_true: int
    test_false: int


@ dataclass
class Monkey:
    items: list[int]
    operation_func: Callable[[int, int], int]
    operation_val: Union[Literal["old"], int]
    test: Test
    items_inspected: int = 0


class MonkeyInventory:
    def __init__(self) -> None:
        self.monkeys: list[Monkey] = []
        self.setup()

    def setup(self) -> None:
        for _, monkey_object in enumerate(inputdata):
            monkey_object_split = monkey_object.split("\n")[1:]
            string_args = list(
                map(str.strip, monkey_object_split)
            )

            starting_items = utils.get_all_digits_re(string_args[0])
            operation = string_args[1].strip().split(": ")[1]
            test_true = string_args[3].strip().split(": ")[1]
            test_false = string_args[4].strip().split(": ")[1]
            test_object = Test(
                divisible_by=utils.get_all_digits_re(string_args[2])[0],
                test_true=int(test_true.split(" ")[-1]),
                test_false=int(test_false.split(" ")[-1])
            )

            operation_expression = operation.split(" = ")[1].split(" ")[1:]
            operation_val: Union[Literal["old"], int] = 0
            try:
                operation_val = int(operation_expression[-1])
            except ValueError:
                operation_val = "old"
            self.monkeys.append(Monkey(
                items=starting_items,
                operation_func=MATH_OPERATORS[operation_expression[0]],
                operation_val=operation_val,
                test=test_object
            ))

    def run(self, rounds_to_run: int, worry_increase: bool, modulo: int) -> None:
        for _ in range(rounds_to_run):
            for _, monkey in enumerate(self.monkeys):
                while len(monkey.items) > 0:
                    monkey.items_inspected += 1
                    item_worry_level = monkey.items[0]
                    operation_val: int = monkey.operation_val if isinstance(
                        monkey.operation_val, int) else item_worry_level
                    new_worry_level = monkey.operation_func(
                        operation_val, item_worry_level)

                    if worry_increase:
                        new_worry_level = new_worry_level // 3
                    else:
                        new_worry_level = new_worry_level % modulo

                    if new_worry_level % monkey.test.divisible_by == 0:  # True
                        self.monkeys[monkey.test.test_true].items.append(
                            new_worry_level)
                    else:
                        self.monkeys[monkey.test.test_false].items.append(
                            new_worry_level)
                    del monkey.items[0]

    def get_monkey_business(self,
                            rounds_to_run: int,
                            worry_increase: bool,
                            modulo: int = 0
                            ) -> int:
        self.run(rounds_to_run, worry_increase, modulo)
        return self.get_monkeys_highest_inspected_sorted()

    def get_monkeys_highest_inspected_sorted(self) -> int:
        two_highest = sorted(
            [x.items_inspected for x in self.monkeys], reverse=True
        )[:2]
        return int(np.multiply(two_highest[0], two_highest[1]))


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    minventory = MonkeyInventory()
    return minventory.get_monkey_business(20, True)


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    minventory = MonkeyInventory()
    modulo = prod([x.test.divisible_by for x in minventory.monkeys])
    return minventory.get_monkey_business(10000, False, modulo)


day_func_arguments = {"split_delimiter": "\n\n"}
# Fixed test data
inputdata = utils.get_day_data(11, test_data=True, **day_func_arguments)
assert part1(silent=True) == 10605  # type: ignore
assert part2(silent=True) == 2713310158  # type: ignore

inputdata = utils.get_day_data(11, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
