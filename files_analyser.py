from loguru import logger

from src.logger import initialize_logger
from src.commands import recursive_search_for_sources


@logger.catch
def main():
    recursive_search_for_sources()


if __name__ == "__main__":
    initialize_logger()
    main()
