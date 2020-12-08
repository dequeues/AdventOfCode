import common  # noqa pylint: disable=unused-import
import utils


def get_input_as_list() -> list[int]:
    with open('2020/day_5/input') as file:
        return [int(line.strip()
                .replace('F', '0')
                .replace('B', '1')
                .replace('L', '0')
                .replace('R', '1'), base=2)
                for line in file.read().split('\n')]


def format_input_to_seat_bin_list(data: list[str]) -> list[int]:
    return [
        int(
            seat.replace('F', '0')
            .replace('B', '1')
            .replace('L', '0')
            .replace('R', '1'), base=2) for seat in data
    ]


seat_list_raw: list[str] = utils.get_day_data(5)
seat_list: list[int] = format_input_to_seat_bin_list(seat_list_raw)


def part1() -> int:
    return max(seat_list)


def part2() -> int:
    seat = 0
    for i in range(min(seat_list), max(seat_list)):
        if (i not in seat_list
                and (i - 1) in seat_list and (i + 1) in seat_list):
            seat = i
            break

    return seat


print(F'Part 1 answer: {part1()}')
print(F'Part 2 answer: {part2()}')
