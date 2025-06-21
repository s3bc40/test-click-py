import click
import enum


class HashType(enum.Enum):
    MD5 = enum.auto()
    SHA1 = enum.auto()


@click.command()
@click.option("--hash-type", type=click.Choice(HashType, case_sensitive=False))
def digest(hash_type: HashType):
    click.echo(hash_type)
