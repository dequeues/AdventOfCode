from dataclasses import dataclass
from typing import Any
import numpy as np
from aoc import utils


@dataclass
class ScenicScore:
    up: int = 0  # pylint: disable=invalid-name
    down: int = 0
    left: int = 0
    right: int = 0

    def prod(self) -> int:
        return self.up * self.down * self.left * self.right


class TreeGrid:
    def __init__(self) -> None:
        _arr = []
        for item in inputdata:
            _arr.append([int(x) for x in item])

        self.arr = np.array(_arr)
        self.height, self.width = self.arr.shape

    def _is_tallest(self, row: int, col: int) -> bool:
        current_tree = self.arr[row, col]
        for i in range(row-1, -1, -1):
            if self.arr[i][col] >= current_tree:
                break
        else:
            return True

        for i in range(row + 1, self.width):
            if self.arr[i][col] >= current_tree:
                break
        else:
            return True

        for neighbour in self.arr[row][:col][::-1]:
            if neighbour >= current_tree:
                break
        else:
            return True

        for neighbour in self.arr[row][col+1:]:
            if neighbour >= current_tree:
                break
        else:
            return True

        return False

    def _get_scenic_score(self, row: int, col: int) -> int:
        current_tree = self.arr[row, col]
        scenic = ScenicScore()

        for i in range(row-1, -1, -1):
            scenic.up += 1
            if self.arr[i][col] >= current_tree:
                break

        for i in range(row + 1, len(self.arr)):
            scenic.down += 1
            if self.arr[i][col] >= current_tree:
                break

        for neighbour in self.arr[row][:col][::-1]:
            scenic.left += 1
            if neighbour >= current_tree:
                break

        for neighbour in self.arr[row][col + 1:]:
            scenic.right += 1
            if neighbour >= current_tree:
                break

        return scenic.prod()

    def get_all_visible_from_outside(self) -> int:
        visible = ((self.height + self.width) * 2) - 4

        for row in range(1, self.width - 1):
            for col in range(1, self.height - 1):
                if self._is_tallest(row, col):
                    visible += 1

        return visible

    def highest_scenic_score_possible(self) -> int:
        highest_score = 0
        for row in range(1, self.width - 1):
            for col in range(1, self.height - 1):
                tree_score = self._get_scenic_score(row, col)
                if tree_score > highest_score:
                    highest_score = tree_score

        return highest_score


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    data = TreeGrid()
    return data.get_all_visible_from_outside()


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    data = TreeGrid()
    return data.highest_scenic_score_possible()


# Fixed test data
inputdata = utils.get_day_data(8, test_data=True)
assert part1(silent=True) == 21  # type: ignore
assert part2(silent=True) == 8  # type: ignore

inputdata = utils.get_day_data(8, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
