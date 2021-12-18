import pytest

from src.files_management.files_search import *
from src.files_management.files_search import get_extension
from src.files_management.files_search import search_valid_files_recursively

class Test_Files_Search:
    def test_get_extension_full_path_given(self):
        input = "~/ASD.d/tsa/KRYCY/plik.txt"
        extension = get_extension(input)
        assert isinstance(extension, str)
        assert extension == ".txt"

    def test_get_extension_only_file_given(self):
        input = "plik.txt"
        extension = get_extension(input)
        assert extension == ".txt"

    def test_get_extension_but_no_extension_given(self):
        input = "/path/to/file"
        extension = get_extension(input)
        assert extension == None

    def test_search_valid_files_recursively(self):
        PARENT_DIRECTORY_PATH = "./fixtures/tests/test_files_search/parent_directory/"
        found_valid_files = search_valid_files_recursively(PARENT_DIRECTORY_PATH)
        assert isinstance(found_valid_files, list)
        assert ["file1.txt", "file2.json", "file3.pcap", "file4.pcap"] == found_valid_files
        INVALID_FILE = "file5.html"
        assert INVALID_FILE not in found_valid_files