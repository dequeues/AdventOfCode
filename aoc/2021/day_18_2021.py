from __future__ import annotations

import json
import math
from copy import deepcopy
from itertools import permutations
from typing import Any
from typing import Optional

from aoc import utils

inputdata: list[Any] = utils.get_day_data(
    18, test_data=False, line_format_func=json.loads
)


class SnailfishNumber:
    left: Optional[SnailfishNumber] = None
    right: Optional[SnailfishNumber] = None
    value: Optional[int] = None
    parent: Optional[SnailfishNumber]

    def __init__(
        self, value: Any, parent: SnailfishNumber | None = None
    ) -> None:
        self.parent = parent
        if isinstance(value, list):
            self.left = SnailfishNumber(value[0], self)
            self.right = SnailfishNumber(value[1], self)
            self.value = None
        else:
            self.value = value

    def search(
        self, current: SnailfishNumber, left: bool = True, right: bool = False
    ) -> SnailfishNumber | None:
        queue, last, exit_next = [self.right, self.left], None, False
        while len(queue) > 0:
            node = queue.pop()

            if node is None:
                continue

            if left and current is node:
                return last

            if node.is_normal:
                if exit_next:
                    return node
                last = node

            if right and current is node:
                exit_next = True

            queue.append(node.right)
            queue.append(node.left)

        return None

    @property
    def depth(self) -> int:
        depth, ancestor = 0, self.parent
        while ancestor is not None:
            depth += 1
            ancestor = ancestor.parent
        return depth

    @property
    def is_normal(self) -> bool:
        return self.value is not None

    @property
    def is_normal_pair(self) -> bool:
        return (
            self.left is not None
            and self.left.is_normal
            and self.right is not None
            and self.right.is_normal
        )

    def reduce(self) -> SnailfishNumber:
        exhausted, has_exploded, has_split = False, False, False
        while not exhausted:
            queue, has_exploded = [self.right, self.left], False
            while len(queue) > 0 and not has_exploded:
                node = queue.pop()

                if node is None:
                    continue

                if node.is_normal_pair and node.depth >= 4:
                    if node.left and node.right:
                        left = self.search(node.left, True, False)
                        right = self.search(node.right, False, True)
                        if (
                            left is not None
                            and left.value is not None
                            and node.left
                            and node.left.value is not None
                        ):
                            left.value += node.left.value
                        if (
                            right is not None
                            and right.value is not None
                            and node.right
                            and node.right.value is not None
                        ):
                            right.value += node.right.value
                        node.value = 0
                        node.left = None
                        node.right = None

                        has_exploded = True

                queue.append(node.right)
                queue.append(node.left)

            if has_exploded:
                continue

            queue, has_split = [self.right, self.left], False
            while len(queue) > 0 and not has_split:
                node = queue.pop()

                if node is None:
                    continue

                if (
                    node.is_normal
                    and isinstance(node.value, int)
                    and node.value >= 10
                ):
                    node.left = SnailfishNumber(
                        math.floor(node.value / 2), node
                    )
                    node.right = SnailfishNumber(
                        math.ceil(node.value / 2), node
                    )
                    node.value = None
                    has_split = True

                queue.append(node.right)
                queue.append(node.left)

            if has_split:
                continue

            exhausted = True

        return self

    @property
    def magnitude(self) -> int:
        if self.is_normal and isinstance(self.value, int):
            return self.value

        if self.left and self.right:
            return 3 * self.left.magnitude + 2 * self.right.magnitude

        return 0

    @property
    def literal(self) -> list[int | Any] | int:
        if self.is_normal and self.value:
            return self.value

        if self.left and self.right:
            return [self.left.literal, self.right.literal]
        return 0

    def add(self, rhs: list[Any]) -> SnailfishNumber:
        node = SnailfishNumber([self.literal, rhs])
        self.parent = node
        return node


@utils.time_func
def part1() -> int:
    data = deepcopy(inputdata)
    root = SnailfishNumber(data.pop(0))
    for line in data:
        root = root.add(line)
        root.reduce()
    return root.magnitude


@utils.time_func
def part2() -> int:
    data = deepcopy(inputdata)
    possible_combinations = list(permutations(data, 2))
    maximum = 0

    for left, right in possible_combinations:
        magnitude = SnailfishNumber(left).add(right).reduce().magnitude
        maximum = max(maximum, magnitude)

    return maximum


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
