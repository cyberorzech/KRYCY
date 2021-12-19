from loguru import logger

from src.logger import initialize_logger
from src.commands import *



@logger.catch
def main():
    recursive_search_for_sources()
    dummy_command()


if __name__ == "__main__":
    initialize_logger()
    main()
