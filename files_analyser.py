from loguru import logger

from src.logger_initializator import initialize_logger
from src.commands import hello, greetings


@logger.catch
def main():
    hello()



if __name__ == "__main__":
    initialize_logger()
    main()
