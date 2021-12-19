from loguru import logger
import pyshark


from src.files_management.files_search import search_valid_files_recursively
from src.files_management.file import File


class PCAP_File(File):
    def __init__(cls, path) -> None:
        super().__init__()
        cls.EXTENSION = ".pcap"
        cls.__path = path

    def read(cls) -> list:
        pcap = pyshark.FileCapture(cls.__path)
        packet_list = [packet for packet in pcap]
        return packet_list


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
