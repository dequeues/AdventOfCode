import re
from functools import cache
from typing import Any

import networkx as nx
from icecream import ic

import aoc.utils.core as utils


class PressureValves:
    valves: dict[str, int]
    minutes: int
    dist: dict[str, int]
    graph: nx.Graph
    shortest_paths: dict[str, dict[str, int]]
    pressure_releases: dict[frozenset[str], int]
    pressure_released: int

    def __init__(self, minutes: int):
        regx: re.Pattern[str] = re.compile(
            r"Valve (\w{2}) has flow rate=(\d*); tunnel[s]? lead[s]? to valve[s]? (.*)")
        self.valves = {}
        self.minutes = minutes
        self.dist = {}
        self.graph = nx.Graph()
        self.shortest_paths = {}
        self.pressure_releases = {}
        self.pressure_released = 0
        for line in inputdata:
            if find_regex := re.search(regx, line):
                valve_name, flow_rate, tunnels_to = find_regex.group(1), int(
                    find_regex.group(2)), find_regex.group(3).split(", ")
                if flow_rate > 0:
                    self.valves[valve_name] = flow_rate

                for tunnel in tunnels_to:
                    self.graph.add_edge(valve_name, tunnel)

        for source, targets in nx.all_pairs_shortest_path_length(self.graph):
            self.shortest_paths[source] = {}
            for target, distance in targets.items():
                if target in self.valves:
                    self.shortest_paths[source][target] = distance + 1

    @cache
    def simulate(
        self,
        minute: int = 1,
        location: str = "AA",
        open_valves: frozenset[tuple[str, int]] = frozenset()
    ) -> int:
        max_released = sum(self.valves[name] * (self.minutes - opened_at)
                           for name, opened_at in open_valves)
        ic(open_valves)

        cur = frozenset([name for name, _ in open_valves])
        ic(self.pressure_releases)
        self.pressure_releases[cur] = self.pressure_releases.get(cur, max_released)
        if self.pressure_releases[cur] < max_released:
            self.pressure_releases[cur] = max_released

        for next_room, distance in self.shortest_paths[location].items():
            if next_room not in [valve[0] for valve in open_valves]:
                if minute + distance <= self.minutes:
                    max_released = max(max_released, self.simulate(
                        minute + distance,
                        next_room,
                        open_valves.union([(next_room, minute + distance - 1)])
                    )
                    )

        return max_released

    def part_one_result(self) -> int:
        return self.simulate()

    def part_two_result(self) -> int:
        self.simulate()
        res_ls: list[tuple[int, frozenset[str]]] = [
            (
                pressure_released,
                open_valves
            ) for open_valves, pressure_released in self.pressure_releases.items()]

        res_ls.sort(key=lambda x: x[0], reverse=True)

        overall_max = 0

        for i, path1 in enumerate(res_ls[:-1]):
            for path2 in res_ls[i+1:]:
                if path1[1].isdisjoint(path2[1]):
                    if path1[0] + path2[0] > overall_max:
                        overall_max = path1[0] + path2[0]
                    else:
                        break
        return overall_max


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return PressureValves(30).part_one_result()


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    return PressureValves(26).part_two_result()


day_func_arguments: dict[str, Any] = {}

# Fixed test data
inputdata = utils.get_day_data(16, test_data=True, **day_func_arguments)
assert part1(silent=True) == 1651  # type: ignore
assert part2(silent=True) == 1707  # type: ignore

inputdata = utils.get_day_data(16, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
