import importlib
import json
import pathlib
from datetime import datetime
from os import utime

import click
import jinja2

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
@ click.option("--stars", "stars", default=0)
def new(day: str, year: int, name: str, stars: int) -> None:
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


    with open("aoc/data/challenges.json") as f:
        data = json.load(f)
        if year not in data:
            data[str(year)] = []
        data = {key: value for key, value in sorted(data.items(), reverse=True)}
        data[str(year)].append({
            "name": name,
            "stars": stars
        })
        with open("README.md", "w+", encoding="utf-8") as file:
            file.write(jinja.get_template("readme.jinja").render({"data": data}))


    click.echo(f"Completed processing for day {day}")


if __name__ == "__main__":
    cli()
