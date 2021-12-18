import click
from loguru import logger

from src.files_management.files_search import search_valid_files_recursively


@click.command()
@click.option("--recursive_search_for_sources", default="no", help="Perform recursive searching for files with extensions specified in ALLOWED_INPUT_FILES_EXTENSIONS")
@click.argument("path")
def recursive_search_for_sources(path, recursive_search_for_sources):
    if recursive_search_for_sources == "no":
        return
    return click.echo(search_valid_files_recursively(parent_directory=path))