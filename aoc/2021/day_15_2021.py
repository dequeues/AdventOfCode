import networkx as netx
import numpy as np
from numpy.typing import NDArray

from aoc import utils


inputdata = utils.get_day_data(15, test_data=False)

SAMPLE_LEN = len(inputdata[0])
ADJS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_numpy_matrix() -> NDArray[np.int_]:
    numpy_graph = np.zeros((SAMPLE_LEN, SAMPLE_LEN), dtype=int)
    for i, line in enumerate(inputdata):
        for j, graph_value in enumerate(line):
            numpy_graph[i, j] = int(graph_value)
    return numpy_graph


@utils.time_func
def part1() -> int:
    numpy_graph = get_numpy_matrix()

    graph = netx.DiGraph()
    for i in range(SAMPLE_LEN):
        for j in range(SAMPLE_LEN):
            for adj_pair in ADJS:
                i_i, i_j = i + adj_pair[0], j + adj_pair[1]
                if 0 <= i_i < SAMPLE_LEN and 0 <= i_j < SAMPLE_LEN:
                    graph.add_edge(
                        (i, j), (i_i, i_j), weight=numpy_graph[i_i, i_j]
                    )

    return int(
        netx.shortest_path_length(
            graph,
            source=(0, 0),
            target=(SAMPLE_LEN - 1, SAMPLE_LEN - 1),
            weight="weight",
        )
    )


@utils.time_func
def part2() -> int:
    ntile = 5
    num_tiles = ntile * SAMPLE_LEN
    graph_tiled = np.zeros((num_tiles, num_tiles), dtype=int)
    graph = netx.DiGraph()
    numpy_graph = get_numpy_matrix()
    for xtile in range(ntile):
        for ytile in range(ntile):
            x_s, y_s = xtile * SAMPLE_LEN, ytile * SAMPLE_LEN
            x_e, y_e = (xtile + 1) * SAMPLE_LEN, (ytile + 1) * SAMPLE_LEN
            offset = xtile + ytile
            graph_tiled[x_s:x_e, y_s:y_e] = (numpy_graph + offset - 1) % 9 + 1

    for i in range(num_tiles):
        for j in range(num_tiles):
            for adj_pair in ADJS:
                if (
                    0 <= i + adj_pair[0] < num_tiles
                    and 0 <= j + adj_pair[1] < num_tiles
                ):
                    graph.add_edge(
                        (i, j),
                        (i + adj_pair[0], j + adj_pair[1]),
                        weight=graph_tiled[i + adj_pair[0], j + adj_pair[1]],
                    )

    return int(
        netx.shortest_path_length(
            graph,
            source=(0, 0),
            target=(num_tiles - 1, num_tiles - 1),
            weight="weight",
        )
    )


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
