from dataclasses import dataclass
from math import ceil
from math import sqrt
from re import match

from aoc import utils


inputdata = utils.get_day_data(17, test_data=False)


@dataclass
class Target:
    x_start: int
    x_end: int
    y_start: int
    y_end: int


class TrickShot:
    def __init__(self, raw_input: str) -> None:
        res = match(
            r"target area: x=(\d*)..(\d*), y=(-?\d*)..(-?\d*)", raw_input
        )
        if res:
            self.target = Target(*list(map(int, res.groups())))

    @property
    def highest_velocity(self) -> int:
        initial = abs(self.target.y_start) - 1
        return initial * (initial + 1) // 2

    @property
    def initial_velocities(self) -> set[tuple[int, int]]:
        _lowest_xs = range(self.__lowest_x(), self.target.x_end + 1)
        _ys = range(self.target.y_start, -self.target.y_start)
        return set(
            (x, y)
            for x in _lowest_xs
            for y in _ys
            if self.__check_xy_velocity(x, y)
        )

    def __lowest_x(self) -> int:
        return ceil(
            (-1 + sqrt(1 ** 2 + 4 * 1 * 2 * self.target.x_start)) / 2 * 1
        )

    def __check_xy_velocity(self, x_coord: int, y_coord: int) -> bool:
        x_pos, y_pos = x_coord, y_coord
        while True:
            if (
                self.target.x_start <= x_pos <= self.target.x_end
                and self.target.y_start <= y_pos <= self.target.y_end
            ):
                return True
            elif x_pos > self.target.x_end or y_pos < self.target.y_start:
                return False

            if x_coord > 0:
                x_coord -= 1
                x_pos += x_coord
            y_coord -= 1
            y_pos += y_coord


@utils.time_func
def part1() -> int:
    trick_shot = TrickShot(inputdata[0])
    return trick_shot.highest_velocity


@utils.time_func
def part2() -> int:
    trick_shot = TrickShot(inputdata[0])
    return len(trick_shot.initial_velocities)


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
