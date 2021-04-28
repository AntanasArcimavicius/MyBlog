import os

import click
import django


@click.group()
def main():
    pass


@click.command()
def hello():
    click.echo("Hello World!")


def setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mb.settings")
    django.setup()

    # Add groups/commands from other modules here after Django setup is done:
    #
    # from mb.foobar import foobar_group
    # main.add_command(foobar_group)
    main.add_command(hello)


setup()
