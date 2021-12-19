import inspect
import pyshark
from loguru import logger

from src.files_management.file import File


class PCAP_File(File):
    def __init__(cls, path) -> None:
        super().__init__()
        cls.EXTENSION = ".pcap"
        cls.path = path

    def read(cls) -> list:
        try:
            if cls.check_extension(cls.EXTENSION, cls.path) == False:
                raise ValueError(
                    f"{inspect.currentframe().f_code.co_name}: invalid file extension. Expects {cls.EXTENSION}, got {cls.path} instead"
                )
            pcap = pyshark.FileCapture(cls.path)
            packet_list = [packet for packet in pcap]
            return packet_list
        except Exception as e:
            logger.error(str(e))


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
