from loguru import logger
from abc import ABC, abstractmethod

from src.settings_getter import get_settings_in_dict

class Files(ABC):
    def __init__(cls) -> None:
        cls.__ALLOWED_EXTENSIONS = get_settings_in_dict["ALLOWED_INPUT_FILES_EXTENSIONS"]

    @abstractmethod
    def read(cls):
        pass

def main():
    raise NotImplementedError("Use as package")

if __name__ == "__main__":
    main()