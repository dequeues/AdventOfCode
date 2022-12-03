import time
from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import TypeVar

from aoc.logger import logger  # type: ignore


@dataclass
class Options:
    split_delimiter: str = "\n"
    test_data: bool = False
    line_format_func: Callable[[str], Any] = lambda x: x


def get_day_data(day: int, **kwargs: Any) -> list[str]:
    day_padded = f"{int(day):02d}"
    options = Options(**kwargs)
    dirname = "input_data" if not options.test_data else "test_data"
    # TODO: Remove hardcoded year
    file_path = f"aoc/2022/{dirname}/day_{day_padded}"
    with open(file_path, encoding="utf-8") as file:
        return [
            options.line_format_func(str(line.strip()))
            for line in file.read().split(options.split_delimiter)
            if line.strip()
        ]


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
        logger.debug(
            f"{func.__name__} function took {(time2-time1)*1000.0:.3f} ms"
        )

        return ret

    return wrap
