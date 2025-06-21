import click


@click.command()
def cli_mod():
    """Prints a hello message."""
    click.echo("Hello, World!")
