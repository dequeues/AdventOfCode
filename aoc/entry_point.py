import importlib
import pathlib
from datetime import datetime
from os import utime

import click
import jinja2

from .logger import logger


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument("day")
@click.option("--day", "day")
@click.option("--year", "year", default=datetime.now().year)
def run(day: str, year: int) -> None:
    day = f"{int(day):02d}"
    logger.info(f"Running day {day} of {year}")
    file_path = pathlib.Path(f"aoc/{year}/day_{day}_{year}.py")
    if file_path.is_file():
        importlib.import_module(f"aoc.{year}.day_{day}_{year}")


@cli.command()
@click.argument("day")
@click.option("--day", "day")
@click.option("--year", "year", default=datetime.now().year)
def new(day: str, year: int) -> None:
    jinja = jinja2.Environment(
        loader=jinja2.PackageLoader("aoc", "templates"),
        keep_trailing_newline=True,
    )

    day = f"{int(day):02d}"

    file_path_script = pathlib.Path(f"aoc/{year}/day_{day}_{year}.py")
    file_path_input = pathlib.Path(f"aoc/{year}/input_data/day_{day}")
    file_path_test_input = pathlib.Path(f"aoc/{year}/test_data/day_{day}")

    try:
        with open(file_path_script, "x", encoding="utf-8") as file:
            file.write(jinja.get_template("new.jinja").render({"day": day}))
    except FileExistsError as error:
        logger.error(f"Could not create {file_path_script}: {error}")

    for f_p in [file_path_input, file_path_test_input]:
        try:
            with open(f_p, "x", encoding="utf-8"):
                utime(f_p, None)
        except FileExistsError as error:
            logger.error(f"Could not create {f_p}: {error}")

    click.echo(f"Completed processing for day {day}")
