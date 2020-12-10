from collections import Counter
import common  # noqa pylint: disable=unused-import
import utils


inputdata: list[int] = sorted(map(int, utils.get_day_data(10)))


def part1() -> int:
    counter = Counter(b - a for a, b in zip([0] + inputdata, inputdata))
    return counter[1] * (counter[3] + 1)


def part2() -> int:
    adapters = [0] + inputdata
    graph = {}
    for i, adapter in enumerate(adapters):
        graph[adapter] = [x for x in adapters[i+1:] if x - adapter <= 3]

    counter = Counter()
    counter[adapters[-1]] = 1

    for adapter in reversed(adapters):
        counter[adapter] += sum([counter[other] for other in graph[adapter]])

    return counter[0]


print(F'Part 1 answer: {part1()}')
print(F'Part 2 answer: {part2()}')
