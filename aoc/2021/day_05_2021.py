from dataclasses import dataclass
from types import SimpleNamespace

import numpy as np

from aoc import utils


inputdata = utils.get_day_data(5, line_format_func=lambda x: x.split(" -> "))


@dataclass
class Vent:
    x_1: int
    y_1: int
    x_2: int
    y_2: int

    @property
    def is_horizontal(self) -> bool:
        return self.y_1 == self.y_2

    @property
    def is_vertical(self) -> bool:
        return self.x_1 == self.x_2

    def line_coords(self):
        vec = np.sign([self.x_2 - self.x_1, self.y_2 - self.y_1])
        coords = SimpleNamespace(**{"x": [self.x_1], "y": [self.y_1]})

        while coords.x[-1] != self.x_2 or coords.y[-1] != self.y_2:
            coords.x.append(coords.x[-1] + vec[0])
            coords.y.append(coords.y[-1] + vec[1])

        return coords.x, coords.y


def part1() -> int:
    vents: list[Vent] = get_formatted_data()
    max_coords = get_max_coords(vents)
    grid = get_grid(max_coords.x, max_coords.y)

    for vent in vents:
        if vent.is_horizontal:
            grid[
                min(vent.x_1, vent.x_2) : max(vent.x_1, vent.x_2) + 1, vent.y_2
            ] += 1
        if vent.is_vertical:
            grid[
                vent.x_1, min(vent.y_1, vent.y_2) : max(vent.y_1, vent.y_2) + 1
            ] += 1
    return np.sum(grid > 1)


def part2() -> int:
    vents: list[Vent] = get_formatted_data()
    max_coords = get_max_coords(vents)
    grid = get_grid(max_coords.x, max_coords.y)

    for vent in vents:
        grid[vent.line_coords()] += 1

    return np.sum(grid > 1)


def get_formatted_data():
    vents = []
    for line in inputdata:
        x_1, y_1 = map(int, line[0].split(","))
        (
            x_2,
            y_2,
        ) = map(int, line[1].split(","))
        vents.append(Vent(x_1, y_1, x_2, y_2))
    return vents


def get_max_coords(vents: list[Vent]) -> SimpleNamespace:
    return SimpleNamespace(
        **{
            "x": max(max(vent.x_1, vent.x_2) for vent in vents) + 1,
            "y": max(max(vent.y_1, vent.y_2) for vent in vents) + 1,
        }
    )


def get_grid(max_x: int, max_y: int):
    return np.zeros((max_x, max_y), int)


print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
