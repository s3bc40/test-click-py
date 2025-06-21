import click


# Using function decorators to define commands
@click.group()
def cli():
    """A simple command line interface."""
    pass


@cli.command()
def initdb():
    click.echo("Initializing the database...")


@cli.command()
def dropdb():
    click.echo("Dropping the database...")


if __name__ == "__main__":
    cli()

# More verbose version or module way if we want to split
# All main group in one file and commands in specific files

# @click.group()
# def cli():
#     pass


# @click.command()
# def initdb():
#     click.echo("Initializing the database...")


# @click.command()
# def dropdb():
#     click.echo("Dropping the database...")


# cli.add_command(initdb)
# cli.add_command(dropdb)
