from loguru import logger

from src.files_management.files_search import search_valid_files_recursively
from src.files_management.files import Files


class TXT_Files(Files):
    def __init__(cls, path) -> None:
        super().__init__()
        cls.path = path

    def read(cls) -> list:
        with open(cls.path) as f:
            txt_line_by_line = f.readlines()
        return txt_line_by_line


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
