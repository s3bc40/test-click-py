import click


@click.command()
@click.option("--count", default=1, help="Number of times to print the message.")
@click.argument("name")
def hello(count, name):
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    for _ in range(count):
        message = f"Hello, {name}! 🐍"
        rainbow_message = "".join(
            [
                click.style(char, fg=colors[i % len(colors)])
                for i, char in enumerate(message)
            ]
        )
        click.echo(rainbow_message)


if __name__ == "__main__":
    hello()
