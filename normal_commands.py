import inspect
import os
import pyshark
from subprocess import check_output
from typing import Union
from re import findall
from loguru import logger
from src.detection_rules import detect_external_dns_request

from src.files_management.pcap_file import PCAP_File
from src.files_management.txt_file import TXT_File
from src.detection_rules import *

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
def open_txt_file(path):
    try:
        if not isinstance(path, str):
            raise TypeError(
                f"{inspect.currentframe().f_code.co_name}: input argument expected string, got {type(path)}"
            )
        txt_file = TXT_File(path)
        txt_file.read()
    except Exception as e:
        logger.error(str(e))


@logger.catch
def bpf_filter(pcap_file_path: str, bpf_filter: str):
    """
    Funkcjonalnosc filtrowania bpf.

    :param pcap_file_path: sciezka do pliku pcap
    :param bpf_filter: filtr, ktory ma zostac zastosowany
    :return: lista przefiltrowanych pakietow
    """
    return pyshark.FileCapture(pcap_file_path, display_filter=bpf_filter)


@logger.catch
def grep_file(
    file_path: str, grep_expr: str, print_flag: bool = False
) -> Union[None, list]:
    """
    Funkcjonalnosc grep.

    :param file_path: sciezka do pliku ktory ma byc zgrepowany
    :param grep_expr: wyrazenie regularne ktore ma byc przekazane do grepa
    :param print_flag: czy wynik polecenia ma byc zwrocony w postaci listy czy wypisany na terminal, defaultowo
    jest zwracany w postaci listy
    :return: None, albo lista w zaleznosci od print_flag
    """
    if print_flag:
        os.system(f'grep "{grep_expr}" {file_path} --text --color')
    else:
        cmd = check_output(f'grep "{grep_expr}" {file_path} --text', shell=True)
        return cmd.decode("ISO-8859-1").split("\n")


@logger.catch
def re_file(file_path: str, regex: str) -> list:
    """
    Funkcjonalnosc re.

    :param file_path: sciezka do pliku na ktorym ma byc wykonane wyrazenie regularne
    :param regex: wyrazenie regularne
    :return: lista wszystkich pasujacych slow
    """
    return findall(f"{regex}", open(file_path).read())

@logger.catch
def run_detection_rules(**kwargs):
    # call all detection rules
    action_alert, action_block, description = detect_external_dns_request(**kwargs)



if __name__ == "__main__":
    open_pcap_file("./fixtures/downloaded_sources/pcap/NASHUA.pcap")
