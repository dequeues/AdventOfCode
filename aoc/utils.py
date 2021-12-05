from dataclasses import dataclass
from typing import Any
from typing import Callable


@dataclass
class Options:
    split_delimiter: str = "\n"
    test_data: bool = False
    line_format_func: Callable[[str], Any] = lambda x: x


def get_day_data(day: int, **kwargs) -> list[str]:
    options = Options(**kwargs)
    dirname = "input_data" if not options.test_data else "test_data"
    file_path = f"aoc/2021/{dirname}/day_{day}"
    with open(file_path, encoding="utf-8") as file:
        return [
            options.line_format_func(str(line.strip()))
            for line in file.read().split(options.split_delimiter)
            if line.strip()
        ]


def convert_list_to_ints(data: list):
    return [int(x) for x in data]
