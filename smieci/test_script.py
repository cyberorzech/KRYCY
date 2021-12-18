import click

from test_group import greet

@click.group()
def group():
    pass


def main():
    group.add_command(greet)
    group()


if __name__ == "__main__":
    main()