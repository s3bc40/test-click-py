import click


@click.command()
def hello():
    """Prints a hello message."""
    click.echo("Hello, World!")


if __name__ == "__main__":
    hello()
