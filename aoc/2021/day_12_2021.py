import networkx as nx

from aoc import utils


inputdata = utils.get_day_data(12, test_data=False)


def build_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_edges_from([line.split("-") for line in inputdata])
    return graph


GRAPH = build_graph()


def traverse(
    node: str,
    part: int = 1,
    path: list[str] | None = None,
    repeat: bool = False,
) -> int:
    if not path:
        path = []
    if node == "start" and node in path:
        return 0
    if node == "end":
        return 1
    if node.isupper() or (node.islower() and node not in path):
        return sum(
            [
                traverse(child, part, path + [node], repeat)
                for child in GRAPH.neighbors(node)
            ]
        )
    if part == 2 and node.islower() and not repeat and path.count(node) == 1:
        return sum(
            [
                traverse(child, part, path + [node], True)
                for child in GRAPH.neighbors(node)
            ]
        )
    return 0


@utils.time_func
def part1() -> int:
    return traverse("start")


@utils.time_func
def part2() -> int:
    return traverse("start", 2)


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
