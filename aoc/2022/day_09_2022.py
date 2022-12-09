from collections import namedtuple
from typing import Any, Literal
from aoc import utils

Move = namedtuple("Move", ["direction", "amount"])


class Bridge:
    def __init__(self) -> None:
        self.moves: list[Move] = []
        self.rope: list[list[int]] = []
        self.setup()

    def setup(self) -> None:
        for line in inputdata:
            direction, amount = line.split(" ")
            self.moves.append(Move(direction, int(amount)))

    def solve(self, knots: int) -> int:
        self.rope = [[0, 0] for _ in range(knots)]
        visited: set[tuple[int, ...]] = {(0, 0)}

        for move in self.moves:
            for _ in range(move.amount):
                self.update_head(move.direction)

                for i in range(1, len(self.rope)):
                    if not self.touching(self.rope[i-1], self.rope[i]):
                        self.update_tail(self.rope[i-1], self.rope[i])
                        if i == knots - 1:
                            visited.add(tuple(self.rope[-1]))

        return len(visited)

    def touching(self, point_one: list[int], point_two: list[int]) -> bool:
        return all([
            abs(point_one[0]-point_two[0]) <= 1,
            abs(point_one[1]-point_two[1]) <= 1
        ])

    def update_head(self, direction: Literal["R", "L", "D", "U"]) -> None:
        head = self.rope[0]
        if direction == "R":
            head[0] += 1
        if direction == "L":
            head[0] -= 1
        if direction == "D":
            head[1] += 1
        if direction == "U":
            head[1] -= 1

    def update_tail(self, previous: list[int], tail: list[int]) -> None:
        if previous[0] < tail[0]:
            tail[0] -= 1
        if previous[0] > tail[0]:
            tail[0] += 1
        if previous[1] < tail[1]:
            tail[1] -= 1
        if previous[1] > tail[1]:
            tail[1] += 1


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    bridge = Bridge()
    return bridge.solve(2)


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    bridge = Bridge()
    return bridge.solve(10)


# Fixed test data
inputdata = utils.get_day_data(9, test_data=True)
assert part1(silent=True) == 13  # type: ignore
inputdata = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")
assert part2(silent=True) == 36  # type: ignore

inputdata = utils.get_day_data(9, test_data=False)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
