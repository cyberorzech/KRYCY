from loguru import logger
from json import loads
from src.files_management.files_search import search_valid_files_recursively
from src.files_management.files import File


class JSON_File(File):
    def __init__(cls, path) -> None:
        super().__init__()
        cls.path = path

    def read(cls) -> dict:
        with open(cls.path) as f:
            json = loads(f.read())
        return json


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
