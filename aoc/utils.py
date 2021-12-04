def get_day_data(
    day: int, split_delimiter: str = "\n", test_data: bool = False
) -> list[str]:
    file_path = (
        f"aoc/2021/{'input_data' if not test_data else 'test_data'}/day_{day}"
    )
    with open(file_path, encoding="utf-8") as file:
        return [
            str(line.strip())
            for line in file.read().split(split_delimiter)
            if line.strip()
        ]


def convert_list_to_ints(data: list):
    return [int(x) for x in data]
