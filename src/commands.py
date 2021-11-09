import click


@click.group()
def greetings():
    pass


@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.argument("name")
def hello(count, name):
    for _ in range(count):
        click.echo(f"Hello {name}!")


@click.command()
def how_ru():
    click.echo("Jak sie masz?")


def main():
    greetings()


if __name__ == "__main__":
    main()
