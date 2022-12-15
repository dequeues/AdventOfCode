import re
from dataclasses import dataclass
from math import inf
from typing import Any

import aoc.utils.core as utils
from aoc.utils.math import manhattan_distance

REGEX_POINT_COORDS = re.compile(
    r"Sensor at x=(?P<sensor_x>-?\d*), y=(?P<sensor_y>-?\d*): closest beacon is at x=(?P<beacon_x>-?\d*), y=(?P<beacon_y>-?\d*)"
)

SENSOR_UPPER_BOUND = 4_000_000


@dataclass
class Point:
    sensor: tuple[int, int]
    beacon: tuple[int, int]


class BeaconExclusionZone:
    points: list[Point]
    sensors: set[tuple[tuple[int, ...], int]]
    beacons: set[tuple[int, ...]]
    max_x: float
    max_y = float
    testing: bool
    measure_line: int
    max_search: int

    def __init__(self, testing: bool) -> None:
        self.points = []
        self.sensors = set()
        self.beacons = set()
        self.min_x, self.max_x = inf, -inf
        self.measure_line = 10 if testing else 2_000_000
        self.max_search = 20 if testing else 4_000_000
        self.setup()

    def setup(self) -> None:
        for line in inputdata:
            match = re.search(REGEX_POINT_COORDS, line)
            if match:
                items = {k: int(v) for k, v in match.groupdict().items()}
                self.points.append(
                    Point(
                        beacon=(items["beacon_x"], items["beacon_y"]),
                        sensor=(items["sensor_x"], items["sensor_y"])
                    )
                )

        for point in self.points:
            dist = manhattan_distance(point.sensor, point.beacon)
            self.sensors.add((tuple(point.sensor), dist))
            self.beacons.add(tuple(point.beacon))
            self.max_x = max(self.max_x, point.sensor[0] + dist)
            self.min_x = min(self.min_x, point.sensor[0] - dist)

    def in_sensor_range(self, test_point: tuple[int, ...]) -> bool:
        for sensor, distance in self.sensors:
            if manhattan_distance(sensor, test_point) <= distance:
                return True
        return False

    def get_total_no_beacon_positions(self) -> int:
        beacons: int = 0
        for idx in range(int(self.min_x), int(self.max_x + 1)):
            test_point: tuple[int, int] = (idx, self.measure_line)
            if test_point not in self.beacons and self.in_sensor_range(test_point):
                beacons += 1

        return beacons

    def get_tuning_frequency(self) -> int:
        answer: int = 0
        sector_multipliers: list[tuple[int, int]] = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for (sensor_x, sensor_y), sensor_distance in self.sensors:
            for sur_dist in range(sensor_distance + 2):
                sur_y = sensor_distance - sur_dist + 1
                for mul_x, mul_y in sector_multipliers:
                    curx, cury = sensor_x + \
                        (sur_dist * mul_x), sensor_y + (sur_y * mul_y)
                    if not 0 <= curx <= self.max_search or\
                            not 0 <= cury <= self.max_search:
                        continue
                    if not self.in_sensor_range((curx, cury)):
                        answer = curx * SENSOR_UPPER_BOUND + cury
        return answer


@utils.time_func
def part1(testing: bool = False, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    exclusion_zone = BeaconExclusionZone(testing)
    return exclusion_zone.get_total_no_beacon_positions()


@ utils.time_func
def part2(testing: bool = False, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    exclusion_zone = BeaconExclusionZone(testing)
    return exclusion_zone.get_tuning_frequency()


day_func_arguments = {}

# Fixed test data
inputdata = utils.get_day_data(15, test_data=True, **day_func_arguments)
assert part1(testing=True, silent=True) == 26  # type: ignore
assert part2(testing=True, silent=True) == 56000011  # type: ignore

inputdata = utils.get_day_data(15, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
