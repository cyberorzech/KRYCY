import os
import pyshark
from subprocess import check_output
from typing import Union
from re import findall


def bpf_filter(pcap_file_path: str, bpf_filter: str):
    """
    Funkcjonalnosc filtrowania bpf.

    :param pcap_file_path: sciezka do pliku pcap
    :param bpf_filter: filtr, ktory ma zostac zastosowany
    :return: lista przefiltrowanych pakietow
    """
    return pyshark.FileCapture(pcap_file_path, display_filter=bpf_filter)


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


def re_file(file_path: str, regex: str) -> list:
    """
    Funkcjonalnosc re.

    :param file_path: sciezka do pliku na ktorym ma byc wykonane wyrazenie regularne
    :param regex: wyrazenie regularne
    :return: lista wszystkich pasujacych slow
    """
    return findall(fr"{regex}", open(file_path).read())
