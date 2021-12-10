from collections import Counter
from typing import List
from typing import Literal

from aoc import utils


inputdata = utils.get_day_data(3)


def part1() -> int:
    gamma, epsilon = 0, 0
    col_values = get_col_values(inputdata)

    gamma = int(
        "".join([Counter(x).most_common()[0][0] for x in col_values]), 2
    )
    epsilon = int(
        "".join([Counter(x).most_common()[-1][0] for x in col_values]), 2
    )

    return gamma * epsilon


def part2() -> int:
    return get_rating("oxy") * get_rating("co2")


def get_col_values(data_list: list[str]) -> list[str]:
    col_values: List[str] = [[] for _ in range(len(data_list[0]))]
    for data in data_list:
        for i, val in enumerate(data):
            col_values[i] += val

    return col_values


def get_rating(gas_type: Literal["co2", "oxy"]) -> int:
    data = inputdata.copy()
    col_values = get_col_values(data)
    criteria = ""
    i = 0
    while len(data) > 1:
        criteria += (
            ("1" if gas_type == "co2" else "0")
            if (col_values[i].count("1") >= len(col_values[i]) / 2)
            else ("0" if gas_type == "co2" else "1")
        )
        data = list(filter(lambda x: x.startswith(criteria), data))
        col_values = get_col_values(data)

        i += 1

    return int(data[0], 2)


print(f"Part 1 answer: {part1()}")
print(f"Part 2 answer: {part2()}")
