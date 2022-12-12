from typing import Any

import networkx.algorithms.shortest_paths as nx_shortest_paths
from networkx import DiGraph

from aoc import utils

LOWERCASE_A_CHAR_VAL = 96


class HeightMap:
    def __init__(self) -> None:
        self.heightmap: dict[list[tuple[int, int]]] = {}
        self.start: tuple[int, int] = tuple()
        self.target:  tuple[int, int] = tuple()
        self.graph: DiGraph = None
        self.setup()
        self.create_graph()

    def setup(self) -> None:
        heightmap = {}
        for row_number, row in enumerate(inputdata):
            for col_number, char in enumerate(row):
                if char == "S":
                    self.start = (row_number, col_number)
                    heightmap[(row_number, col_number)] = ord("a")
                elif char == "E":
                    self.target = (row_number, col_number)
                    heightmap[(row_number, col_number)] = ord("z")
                else:
                    heightmap[(row_number, col_number)] = ord(char)

        self.heightmap = heightmap

    def create_graph(self) -> None:
        graph = DiGraph()
        for (row_number, col_number), char_val in self.heightmap.items():
            for x_point, y_point in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if self.heightmap.get(
                    (row_number + x_point, col_number + y_point), 999
                ) <= (char_val + 1):
                    graph.add_edge(
                        (row_number, col_number),
                        (row_number + x_point, col_number + y_point)
                    )
        self.graph = graph

    def get_fewest_steps(self) -> int:
        return len(
            nx_shortest_paths.shortest_path(
                self.graph, source=self.start, target=self.target)
        ) - 1

    def get_steps_for_best_signal(self) -> int:
        all_steps = []
        for _, steps in nx_shortest_paths.single_target_shortest_path(
            self.graph, self.target, cutoff=self.get_fewest_steps()
        ).items():
            if self.heightmap.get(steps[0]) == LOWERCASE_A_CHAR_VAL + 1:
                all_steps.append(len(steps))

        return min(all_steps) - 1


@ utils.time_func
def part1(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    heightmap = HeightMap()
    return heightmap.get_fewest_steps()


@ utils.time_func
def part2(*args: Any, **kwargs: Any) -> int:  # pylint: disable=unused-argument
    heightmap = HeightMap()
    return heightmap.get_steps_for_best_signal()


day_func_arguments = {}

# Fixed test data
inputdata = utils.get_day_data(12, test_data=True, **day_func_arguments)
assert part1(silent=True) == 31  # type: ignore
assert part2(silent=True) == 29  # type: ignore

inputdata = utils.get_day_data(12, test_data=False, **day_func_arguments)
utils.print_result(F'Part 1 answer: {part1()}')
utils.print_result(F'Part 2 answer: {part2()}')
