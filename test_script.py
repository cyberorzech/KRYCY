from loguru import logger

from src.logger_initializator import initialize_logger
from src.commands import hello, greetings, how_ru


@logger.catch
def main():
    how_ru()



if __name__ == "__main__":
    initialize_logger()
    main()
