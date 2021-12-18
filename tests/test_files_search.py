import pytest

from src.files_management.files_search import *
from src.files_management.files_search import get_extension

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