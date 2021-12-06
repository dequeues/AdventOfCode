import functools

from aoc import utils


inputdata = utils.get_day_data(6, split_delimiter=",", test_data=False)


def part1() -> int:
    return sum(simulate(n, 80) for n in list(map(int, inputdata.copy())))


def part2() -> int:
    return sum(simulate(n, 256) for n in list(map(int, inputdata.copy())))


@functools.lru_cache(maxsize=None)
def simulate(days_until_spawn: int, sim_length: int) -> int:
    if sim_length < 1:
        return 1
    if days_until_spawn == 0:
        return simulate(6, sim_length - 1) + simulate(8, sim_length - 1)

    return simulate(0, sim_length - days_until_spawn)


print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
