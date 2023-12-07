import importlib
import pathlib
from datetime import datetime
from os import utime

import click
import jinja2
import pandoc
from pandoc.types import Header, Link, Plain, Space, Str, Table

from .logger import logger


@ click.group()
def cli() -> None:
    pass


@ cli.command()
@ click.argument("day")
@ click.option("--day", "day")
@ click.option("--year", "year", default=datetime.now().year)
def run(day: str, year: int) -> None:
    day = f"{int(day):02d}"
    logger.info(f"Running day {day} of {year}")
    file_path = pathlib.Path(f"aoc/{year}/day_{day}_{year}.py")
    if file_path.is_file():
        importlib.import_module(f"aoc.{year}.day_{day}_{year}")
    else:
        logger.error(f"{file_path} does not exist.")


@ cli.command()
@ click.argument("day")
@ click.option("--day", "day")
@ click.argument("name")
@ click.option("--name", "name")
@ click.option("--year", "year", default=datetime.now().year)
def new(day: str, year: int, name: str) -> None:
    jinja = jinja2.Environment(
        loader=jinja2.PackageLoader("aoc", "templates"),
        keep_trailing_newline=True,
    )
    day_padded = f"{int(day):02d}"

    file_path_script = pathlib.Path(f"aoc/{year}/day_{day_padded}_{year}.py")
    file_path_input = pathlib.Path(f"aoc/{year}/input_data/day_{day_padded}")
    file_path_test_input = pathlib.Path(f"aoc/{year}/test_data/day_{day_padded}")

    try:
        with open(file_path_script, "x", encoding="utf-8") as file:
            file.write(jinja.get_template("new.jinja").render({"day": day}))
    except (FileExistsError, FileNotFoundError) as error:
        logger.error(file_path_script.resolve())
        logger.error(f"Could not create {file_path_script}: {error}")

    for f_p in [file_path_input, file_path_test_input]:
        try:
            with open(f_p, "x", encoding="utf-8"):
                utime(f_p, None)
        except FileExistsError as error:
            logger.error(f"Could not create {f_p}: {error}")

    # TODO: This doesn't seem to work, and I have no idea why. Maybe for another time? Maybe not. Who knows.
    # readme_path = pathlib.Path("README.md")

    # with open(readme_path.resolve(), "r", encoding="utf-8") as file_handler:
    #     pandoc_data = pandoc.read(file_handler.read())

    # heading_index: int = 0
    # # Find index for the year heading
    # for element, path in pandoc.iter(pandoc_data, path=True):
    #     if element != pandoc_data:
    #         if isinstance(element, Header):
    #             if element[2][0][0] == str(year):
    #                 _, heading_index = path[-1]

    # Stderr:       | JSON parse error: Error in $.blocks[11][1]: cannot unpack array of length 1 into a tuple of length 3
    # HUH?

    # pandoc_data[1][heading_index+1][4].insert(
    #     len(pandoc_data[1][heading_index+1][4]) + 1,
    #     [
    #         [Plain([Link(('', [], []), [Str(day_padded)],
    #                      (f"https://adventofcode.com/{year}/day/{day}", ''))])],
    #         [Plain([Str(name)])],
    #         [Plain([Link(('', [], []), [Str(f"{file_path_script}")],
    #                      (f"/{file_path_script}", ''))])],
    #         [Plain([Str('')])]
    #     ]
    # )

    # pandoc.write(pandoc_data, readme_path, "gfm")

    click.echo(f"Completed processing for day {day}")


if __name__ == "__main__":
    cli()
