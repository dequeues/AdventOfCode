def get_day_data(day: int, split_delimiter: str = "\n") -> list[str]:
    with open(f"aoc/2021/input_data/day_{day}") as file:
        return [
            str(line.strip())
            for line in file.read().split(split_delimiter)
            if line.strip()
        ]


def convert_list_to_ints(data: list):
    return [int(x) for x in data]
