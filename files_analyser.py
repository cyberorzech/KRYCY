import click
from loguru import logger
from src.commands import (
    bpf_filter,
    grep_file,
    open_pcap_file,
    open_txt_file,
    re_file,
    recursive_search_for_sources,
)

from src.logger import initialize_logger


@click.command()
@click.option(
    "--recursive_search_for_sources",
    default="no",
    help="Perform recursive searching for files with extensions specified in ALLOWED_INPUT_FILES_EXTENSIONS",
)
@click.option("--open", default="no", help="Opens a file (choose pcap or txt)")
@click.option(
    "--filter",
    default="no",
    help="Specifies filter for opening file (choose bpf, grep or re)",
)
@click.option("--filter_value", help="Filter")
@click.argument("working_directory", default="./", required=False)
def cli(**kwargs):
    path = kwargs["working_directory"]
    """KRYCY LAB1A (:"""
    if kwargs["recursive_search_for_sources"] == "yes":
        recursive_search_for_sources(path)

    if kwargs["open"] == "pcap":
        if kwargs["filter"] == "bpf":
            bpf_filter(path, kwargs["filter_value"])

        elif kwargs["filter"] == "grep":
            grep_file(path, kwargs["filter_value"])
        elif kwargs["filter"] == "re":
            re_file(path, kwargs["filter_value"])
        else:
            open_pcap_file(path)

    if kwargs["open"] == "txt":
        if kwargs["filter"] == "bpf":
            bpf_filter(path, kwargs["filter_value"])

        elif kwargs["filter"] == "grep":
            grep_file(path, kwargs["filter_value"])
        elif kwargs["filter"] == "re":
            re_file(path, kwargs["filter_value"])
        else:
            open_txt_file(path)


if __name__ == "__main__":
    initialize_logger()
    cli()
