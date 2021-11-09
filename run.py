from loguru import logger
from src.logger_initializator import initialize_logger


@logger.catch
def main():
    pass
    logger.info("Test")


if __name__ == "__main__":
    initialize_logger()
    main()
