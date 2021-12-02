import importlib
import pathlib
from datetime import datetime
from os import utime

import click
import jinja2


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument("day")
@click.option("--day", "day")
@click.option("--year", "year", default=datetime.now().year)
def run(day: int, year: int) -> None:
    print(f"Running day {day} of {year}")
    file_path = pathlib.Path(f"aoc/{year}/day_{day}_{year}.py")
    if file_path.is_file():
        importlib.import_module(f"aoc.{year}.day_{day}_{year}")


@cli.command()
@click.argument("day")
@click.option("--day", "day")
@click.option("--year", "year", default=datetime.now().year)
def new(day: int, year: int) -> None:
    jinja = jinja2.Environment(
        loader=jinja2.PackageLoader("aoc", "templates"),
        keep_trailing_newline=True,
    )

    file_path_script = pathlib.Path(f"aoc/{year}/day_{day}_{year}.py")
    file_path_input = pathlib.Path(f"aoc/{year}/input_data/day_{day}")

    try:
        with open(file_path_script, "x", encoding="utf-8") as file:
            file.write(jinja.get_template("new.jinja").render({"day": day}))
    except FileExistsError as error:
        print(f"Could not create {file_path_script}: {error}")

    try:
        with open(file_path_input, "x", encoding="utf-8"):
            utime(file_path_input, None)
    except FileExistsError as error:
        print(f"Could not create {file_path_input}: {error}")

    click.echo(f"Completed processing for day {day}")
