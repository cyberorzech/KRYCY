from loguru import logger

from src.files_management.files_search import search_valid_files_recursively
from src.files_management.files import Files

class PCAP_Files(Files):
    def __init__(cls) -> None:
        super().__init__()

    def read(cls) -> list:
        pass

def main():
    raise NotImplementedError("Use as package")

if __name__ == "__main__":
    main()