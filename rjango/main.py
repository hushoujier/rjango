# -*- coding:utf-8 -*-
"""
@Time             : 2025-01-24
@Email            : hushoujier@qq.com
@Author           : 胡守杰
@FileName         : main.py
@ZhDescription    :
@EnDescription    :
"""
import datetime
import os
import shutil
import sys
from pathlib import Path
from typing import Iterator

from django.core.management import call_command
from typer import Typer, Option

from rjango import utils
from rjango.core.commands.inspectdb import InspectDB
from rjango.core.commands.sqlmigrate import SQLMigrate
from rjango.core.decorators import setup_django

application = Typer()


@application.command()
def init(
        example: bool = Option(
            default=False,
            help='Whether to include a example file',
            prompt='Whether to include a example file',
            show_default=True)
):
    """
    Initialize the migration folder
    """
    template = f'{Path(__file__).resolve().parent.parent / "migrations_template/empty"}'
    if example:
        template = f'{Path(__file__).resolve().parent.parent / "migrations_template/example"}'
    target = utils.get_target()
    shutil.copytree(template, target)


@application.command()
@setup_django
def add():
    """
    Add migration file
    """
    call_command(
        'makemigrations',
        name=f'created{datetime.datetime.now().strftime("%Y%m%d")}',
        interactive=False)
    migrations: Iterator[Path] = filter(
        lambda migration: migration.suffix == '.py' and migration.name != '__init__.py',
        Path(f'{utils.get_target()}/migrations').iterdir())

    for migration in migrations:
        description = migration.name.split('.')[0]
        up_sql = call_command(SQLMigrate(), 'migrations', description)
        with open(f'migrations/{description}.up.sql', 'w+', encoding='utf-8') as file:
            file.write(up_sql)
        down_sql = call_command(SQLMigrate(), 'migrations', '--backwards', description)
        with open(f'migrations/{description}.down.sql', 'w+', encoding='utf-8') as file:
            file.write(down_sql)


@application.command()
@setup_django
def inspect():
    """
    Generate models in reverse using database tables
    """
    target = utils.get_target()
    stdout = os.path.join(target, 'models', '__init__.py')
    with open(stdout, 'w+', encoding='utf-8') as file:
        call_command(InspectDB(), stdout=file)


@application.command()
@setup_django
def debug():
    """
    Obtaining Debugging information
    """
    from rich import print  # pylint:disable=redefined-builtin,import-outside-toplevel
    from django.conf import settings  # pylint: disable=import-outside-toplevel
    print('OS information:')
    print(os.uname())
    print('OS environ:')
    print(os.environ)

    print('Python version:')
    print(sys.version)
    print('Python package path:')
    print(sys.path)
    print('Django settings:')
    print(settings.__dict__)
    print('Django BASE_DIR:')
    print(settings.BASE_DIR)


if __name__ == '__main__':
    application()
