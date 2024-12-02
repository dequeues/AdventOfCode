import time
from dataclasses import dataclass
from datetime import date
from inspect import stack
from re import findall, search
from typing import Any, Callable, ParamSpec, TypeAlias, TypedDict, TypeVar

from pydantic_settings import BaseSettings

from aoc.logger import logger  # type: ignore

T = TypeVar("T", str, list[int])

LineFormatFuncType = Callable[[str], Any]  # pyright: ignore[reportExplicitAny]


def _default_line_format_func(line: Any) -> Any:  # pyright: ignore[reportExplicitAny, reportAny]
    return line  # pyright: ignore[reportAny]


class DaySettings(BaseSettings):
    split_delimiter: str = "\n"
    test_data: bool = False
    line_format_func: LineFormatFuncType = _default_line_format_func

    no_strip: bool = False


@dataclass
class Options:
    split_delimiter: str = "\n"
    test_data: bool = False
    part_two: bool | None = False
    line_format_func: LineFormatFuncType = _default_line_format_func

    no_strip: bool = False


class Challenge(TypedDict):
    name: str
    stars: int


ChallengeList: TypeAlias = dict[str, list[Challenge]]

DayDataT: TypeAlias = list[str] | list[int] | list[list[int]]


class DayData(TypedDict):
    test_data: DayDataT
    data: DayDataT


def get_day_data(
    day: int, day_settings: DaySettings | None = None, **kwargs: int
) -> DayDataT:
    options: Options | DaySettings
    if not day_settings:
        options = Options(**kwargs)  # pyright: ignore[reportArgumentType]
    else:
        options = day_settings
    day_padded = f"{int(day):02d}"
    dirname = "input_data" if not kwargs.get("test_data", False) else "test_data"
    year_re = search(r"day_\d*_(\d{4}).py", stack()[1].filename)
    if year_re:
        year = year_re.group(1)
    else:
        year = str(date.today().year)

    if isinstance(options, Options) and options.part_two:
        file_path = f"aoc/{year}/{dirname}/day_{day_padded}_2"
    else:
        file_path = f"aoc/{year}/{dirname}/day_{day_padded}"

    with open(file_path, encoding="utf-8") as file:
        lines: list[str] = []
        for line in file.read().split(options.split_delimiter):
            line_formatted: str = options.line_format_func(
                str(line.strip()) if not options.no_strip else line
            )
            lines.append(line_formatted)
        return lines


def convert_list_to_ints(data: list[str]) -> list[int]:
    return [int(x) for x in data]


def print_result(message: str) -> None:
    logger.opt(depth=1, colors=True).success(message)


P = ParamSpec("P")
R = TypeVar("R")


def time_func(func: Callable[P, R]) -> Callable[P, R]:
    def wrap(*args: P.args, **kwargs: P.kwargs) -> R:
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
