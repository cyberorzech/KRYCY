import sys
from loguru import logger
from datetime import date
from src.settings_getter import get_settings_in_dict


def initialize_logger():
    LOG_FILE_EXTENSION = ".log"
    SETTINGS = get_settings_in_dict()
    logger.add(
        sys.stderr,
        colorize=True,
        format="{time} {level} {message}",
        filter="my_module",
        level=SETTINGS["LOG_LEVEL"],
    )
    day = date.today()
    log_filename = day.strftime("%b-%d-%Y") + LOG_FILE_EXTENSION
    logger.add(SETTINGS["LOG_DIRECTORY"] + log_filename)


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
