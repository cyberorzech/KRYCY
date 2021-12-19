from loguru import logger
from xmltodict import parse
import xml.etree.ElementTree as ET
from json import dumps, loads
from src.files_management.files_search import search_valid_files_recursively
from src.files_management.files import Files


class XML_Files(Files):
    def __init__(cls, path) -> None:
        super().__init__()
        cls.path = path

    def read(cls) -> dict:
        tree = ET.parse(cls.path)
        root = tree.getroot()
        return loads(dumps(parse(ET.tostring(root, encoding="utf8", method="xml"))))


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
