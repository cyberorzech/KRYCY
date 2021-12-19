from loguru import logger
from src.commands import open_pcap_file

from src.logger import initialize_logger
from src.commands import *


@logger.catch
def main():
    # recursive_search_for_sources()
    # dummy_command()
    open_pcap_file("asd")


if __name__ == "__main__":
    initialize_logger()
    main()
