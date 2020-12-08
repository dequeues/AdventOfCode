import os
import sys
import pathlib
import importlib
from glob import glob
import re
import click
import jinja2
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                '2020/'))


def get_all_day_files() -> list[str]:
    return [re.search(r'day_(\w+).py', str(file)).groups()[0]
            for file in glob('aoc/2020/day_*.py')
            ]


all_days_as_list: list[str] = get_all_day_files()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('day')
@click.option('--day', 'day',
              type=click.Choice(all_days_as_list, case_sensitive=False)
              )
def run(day: int):
    file_path = pathlib.Path(F'aoc/2020/day_{day}.py')
    if file_path.is_file():
        importlib.import_module(F'aoc.2020.day_{day}')


@cli.command()
@click.argument('day', default=len(all_days_as_list)+1)
@click.option('--day', 'day', default=len(all_days_as_list)+1)
def new(day: int) -> None:
    jinja = jinja2.Environment(
        loader=jinja2.PackageLoader('aoc', 'templates')
    )

    file_path_script = pathlib.Path(F'aoc/2020/day_{day}.py')
    file_path_input = pathlib.Path(F'aoc/2020/input_data/day_{day}')

    try:
        with open(file_path_script, 'x') as file:
            file.write(jinja.get_template('new.jinja').render())
    except FileExistsError as error:
        print(F'Could not create {file_path_script}: {error}')

    try:
        open(file_path_input, 'x').close()
    except FileExistsError as error:
        print(F'Could not create {file_path_input}: {error}')

    click.echo(F'Completed processing for day {day}')
