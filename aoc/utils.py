from dataclasses import dataclass
from typing import Any
from typing import Callable

from .logger import logger


@dataclass
class Options:
    split_delimiter: str = "\n"
    test_data: bool = False
    line_format_func: Callable[[str], Any] = lambda x: x


def get_day_data(day: int, **kwargs) -> list[str]:
    day_padded = f"{int(day):02d}"
    options = Options(**kwargs)
    dirname = "input_data" if not options.test_data else "test_data"
    file_path = f"aoc/2021/{dirname}/day_{day_padded}"
    with open(file_path, encoding="utf-8") as file:
        return [
            options.line_format_func(str(line.strip()))
            for line in file.read().split(options.split_delimiter)
            if line.strip()
        ]


def convert_list_to_ints(data: list):
    return [int(x) for x in data]


def print_result(message: str):
    logger.opt(depth=1, colors=True).success(message)
