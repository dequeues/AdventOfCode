from typing import Tuple

import numpy as np
import numpy.typing as npt

from aoc import utils

inputdata = utils.get_day_data(11, test_data=False)


def get_matrix() -> npt.NDArray[np.int_]:
    return np.array(
        [[int(x) for x in line.strip()] for line in inputdata.copy()],
        dtype=int,
    )


def flash(
    matrix: npt.NDArray[np.int_],
    x_coord: int,
    y_coord: int,
    flashes: list[Tuple[int, int]],
) -> None:
    matrix[x_coord][y_coord] = 0
    flashes.append((x_coord, y_coord))

    for i in [x_coord - 1, x_coord, x_coord + 1]:
        for j in [y_coord - 1, y_coord, y_coord + 1]:
            if (i, j) not in flashes and i >= 0 and j >= 0:
                try:
                    matrix[i][j] += 1
                    if matrix[i][j] > 9:
                        flash(matrix, i, j, flashes)
                except IndexError:
                    continue


def step(matrix: npt.NDArray[np.int_]) -> int:
    flashes: list[Tuple[int, int]] = []

    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[0]):
            matrix[i][j] += 1

    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[0]):
            if matrix[i][j] > 9:
                flash(matrix, i, j, flashes)

    return len(flashes)


@utils.time_func
def part1() -> int:
    matrix = get_matrix()
    return sum([step(matrix) for _ in range(100)])


@utils.time_func
def part2() -> int:
    days = 100
    matrix = get_matrix()
    _ = [step(matrix) for _ in range(100)]
    while matrix.any():
        step(matrix)
        days += 1
    return days


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
