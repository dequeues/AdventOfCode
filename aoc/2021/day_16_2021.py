from functools import reduce
from typing import Callable

from aoc import utils

inputdata = utils.get_day_data(16, test_data=False)


TYPES: dict[int, Callable[..., int]] = {
    0: sum,
    1: lambda *args: reduce(lambda x, y: x * y, *args, 1),  # type: ignore
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[0]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}

VERSION_NUMBERS = []


def get_bin_data() -> str:
    data = f"{int(inputdata[0], 16):08b}"
    data = ("0" * (4 - num) + data) if (num := len(data) % 4) else data
    return data


def literal_value(packet: str) -> tuple[int, str]:
    value = ""
    while packet[0] == "1":
        value += packet[1:5]
        packet = packet[5:]

    value += packet[1:5]
    return int(value, 2), packet[5:]


def parse(packet: str) -> tuple[int, str]:
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    packet = packet[6:]

    value = 0
    VERSION_NUMBERS.append(version)

    if type_id == 4:  # Literal Value
        value, packet = literal_value(packet)
    elif type_id != 4:  # Operator
        length_id, packet = packet[0], packet[1:]
        values = []

        if length_id == "0":
            length_bits, packet = int(packet[:15], 2), packet[15:]
            sub_packet, packet = packet[:length_bits], packet[length_bits:]
            while sub_packet:
                val, sub_packet = parse(sub_packet)
                values.append(val)

        elif length_id == "1":
            num_subs, packet = int(packet[:11], 2), packet[11:]
            for _ in range(0, num_subs):
                val, packet = parse(packet)
                values.append(val)

        value = TYPES[type_id](values)

    return value, packet


@utils.time_func
def part1() -> int:
    _ = parse(get_bin_data())
    return sum(VERSION_NUMBERS)


@utils.time_func
def part2() -> int:
    # 562406347874 too low
    return parse(get_bin_data())[0]


utils.print_result(f"Part 1 answer: {part1()}")
utils.print_result(f"Part 2 answer: {part2()}")
