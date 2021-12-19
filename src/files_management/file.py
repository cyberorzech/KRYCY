import inspect
import re
from loguru import logger
from abc import ABC, abstractmethod

from src.settings_getter import get_settings_in_dict


class File(ABC):
    def __init__(cls) -> None:
        cls.__ALLOWED_EXTENSIONS = get_settings_in_dict()[
            "ALLOWED_INPUT_FILES_EXTENSIONS"
        ]

    @logger.catch
    def check_extension(cls, extension, path_to_file) -> bool:
        NO_DOT_IN_EXTENSION = -1
        try:
            if not isinstance(extension, str) or not isinstance(path_to_file, str):
                raise TypeError(f"{inspect.currentframe().f_code.co_name}: input arguments expected string, got {type(extension)}")
            if extension.find(".") == NO_DOT_IN_EXTENSION:
                raise ValueError(f"{inspect.currentframe().f_code.co_name}: extension argument has to be passed with dot, got {extension} instead")
            regex = f"({extension})"
            m = re.search(regex, path_to_file)
            if m == None:
                return False
            return True
        except Exception as e:
            logger.error(str(e))

    @abstractmethod
    def read(cls):
        pass



def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
