from collections import namedtuple
from typing import Any

from aoc import utils

Point = namedtuple("Point", "x y")


class Cave:
    sand: set[Point]
    paths: list[list[Point]]
    stones: set[Point]
    y_max: int
    source: Point

    def __init__(self) -> None:
        self.paths = []
        for path in inputdata:
            ints = utils.parse_ints(path)
            self.paths.append([
                Point(ints[i], ints[i+1]) for i in range(0, len(ints), 2)
            ])
        self.stones = self.get_stones()

        self.sand = set()
        self.y_max = max([p.y for p in self.stones])
        self.source = Point(500, 0)

    def get_stones(self) -> set[Point]:
        stones: set[Point] = set()
        for points in self.paths:
            for i in range(len(points) - 1):
                self.draw_line(stones, points[i], points[i + 1])
        return stones

    def drop_sand(
        self,
        source: Point,
        stones: set[Point],
        sand: set[Point],
        y_max: int
    ) -> Point:
        stones_or_sand = stones.union(sand)
        start = source
        while start.y < y_max:
            p_down = Point(start.x, start.y + 1)
            p_down_left = Point(start.x - 1, start.y + 1)
            p_down_right = Point(start.x + 1, start.y + 1)
            if p_down not in stones_or_sand:
                start = p_down
            elif p_down_left not in stones_or_sand:
                start = p_down_left
            elif p_down_right not in stones_or_sand:
                start = p_down_right
            else:
                break
        return start

    def draw_line(self, pixels: set[Point], start: Point, end: Point) -> None:
        line_x = end.x - start.x
        line_y = end.y - start.y

        line_x = 1 if line_x > 0 else -1 if line_x < 0 else 0
        line_y = 1 if line_y > 0 else -1 if line_y < 0 else 0

        pos = start
        pixels.add(pos)
        while pos != end:
            pos = Point(pos.x + line_x, pos.y + line_y)
            pixels.add(pos)

    def simulate_sand(self, resting: bool = False) -> None:
        while True:
            pos = self.drop_sand(self.source, self.stones, self.sand, self.y_max + 1)
            if resting:
                self.sand.add(pos)
                if pos.y == self.source.y:
                    break
            else:
                if pos.y >= self.y_max:
                    break
                self.sand.add(pos)

    def get_total_sandfall_before_abyss(self) -> int:
        self.simulate_sand()
        return len(self.sand)

    def get_sand_resting_amount(self) -> int:
        self.simulate_sand(True)
        return len(self.sand)


@utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    cave = Cave()
    return cave.get_total_sandfall_before_abyss()


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    cave = Cave()
    return cave.get_sand_resting_amount()


day_func_arguments: dict[str, str] = {}

# Fixed test data
inputdata = utils.get_day_data(14, test_data=True, **day_func_arguments)
assert part1(silent=True) == 24  # type: ignore
assert part2(silent=True) == 93  # type: ignore

inputdata = utils.get_day_data(14, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
