import time
from dataclasses import dataclass
from datetime import date
from inspect import stack
from re import findall, search
from typing import Any, Callable, Optional, TypeVar

from pydantic import BaseSettings

from aoc.logger import logger  # type: ignore


class DaySettings(BaseSettings):
    split_delimiter: str = "\n"
    test_data: bool = False

    def line_format_func(x: str) -> Any:
        return x

    no_strip: bool = False


@dataclass
class Options:
    split_delimiter: str = "\n"
    test_data: bool = False
    part_two: Optional[bool] = False

    def line_format_func(x: str) -> Any:
        return x

    no_strip: bool = False


def get_day_data(
    day: int, day_settings: Optional[DaySettings] = None, **kwargs: Any
) -> list[str]:
    options: Options | DaySettings
    if not day_settings:
        options = Options(**kwargs)
    else:
        options = day_settings
    day_padded = f"{int(day):02d}"
    dirname = "input_data" if not options.test_data else "test_data"
    year_re = search(r"day_\d*_(\d{4}).py", stack()[1].filename)
    if year_re:
        year = year_re.group(1)
    else:
        year = str(date.today().year)

    if options.part_two:
        file_path = f"aoc/{year}/{dirname}/day_{day_padded}_2"
    else:
        file_path = f"aoc/{year}/{dirname}/day_{day_padded}"

    with open(file_path, encoding="utf-8") as file:
        lines = []
        for line in file.read().split(options.split_delimiter):
            line_formatted = options.line_format_func(
                str(line.strip()) if not options.no_strip else line
            )
            lines.append(line_formatted)
        return lines


def convert_list_to_ints(data: list[str]) -> list[int]:
    return [int(x) for x in data]


def print_result(message: str) -> None:
    logger.opt(depth=1, colors=True).success(message)


T = TypeVar("T")  # pylint: disable=invalid-name


def time_func(func: Any) -> Callable[..., Callable[..., T]]:
    def wrap(*args: Any, **kwargs: Any) -> Any:
        time1 = time.time()
        ret = func(*args, **kwargs)
        time2 = time.time()
        if not kwargs.get("silent"):
            logger.debug(f"{func.__name__} function took {(time2-time1)*1000.0:.3f} ms")

        return ret

    return wrap


def get_all_digits_re(string_to_evaluate: str) -> list[int]:
    return list(map(int, findall(r"\d+", string_to_evaluate)))


def parse_ints(string: str) -> tuple[int, ...]:
    groups = findall(r"-?\d+", string)
    return tuple(map(int, groups))
