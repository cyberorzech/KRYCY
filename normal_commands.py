import inspect
from loguru import logger

from src.files_management.pcap_file import PCAP_File

# to be implemented with click
@logger.catch
def open_pcap_file(path):
    try:
        if not isinstance(path, str):
            raise TypeError(
                f"{inspect.currentframe().f_code.co_name}: input argument expected string, got {type(path)}"
            )
        pcap_file = PCAP_File(path)
        pcap_file.read()

    except Exception as e:
        logger.error(str(e))


@logger.catch
def grep_on_txt_file(path):
    pass


@logger.catch
def re_on_text_file(path):
    pass


if __name__ == "__main__":
    open_pcap_file("./fixtures/downloaded_sources/pcap/NASHUA.pcap")
