from loguru import logger
import Evtx.Evtx as evtx
import xmltodict
from json import loads, dumps
from src.files_management.files_search import search_valid_files_recursively
from src.files_management.files import Files

class EVTX_Files(Files):
    def __init__(cls, path) -> None:
        super().__init__()
        cls.path = path

    def read(cls) -> list:
        list_with_log_dicts = list()
        with evtx.Evtx(cls.path) as log:
            for record in log.records():
                list_with_log_dicts.append(loads(dumps((xmltodict.parse((record.xml()))))))
        return list_with_log_dicts

def main():
    raise NotImplementedError("Use as package")

if __name__ == "__main__":
    main()