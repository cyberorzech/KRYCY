import click
from loguru import logger

from src.files_management.files_search import search_valid_files_recursively
from src.logger import insert_log_to_db


@click.command()
@click.option(
    "--recursive_search_for_sources",
    default="no",
    help="Perform recursive searching for files with extensions specified in ALLOWED_INPUT_FILES_EXTENSIONS",
)
@click.argument("path")
def recursive_search_for_sources(path, recursive_search_for_sources):
    if recursive_search_for_sources == "no":
        return
    command_result = search_valid_files_recursively(parent_directory=path)
    command_usage_message = "Performed recursive_search_for_sources"
    logger.info(f"{command_usage_message}: {command_result}")
    insert_log_to_db(command_usage_message)
    click.echo(command_result)
