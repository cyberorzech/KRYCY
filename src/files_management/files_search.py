from loguru import logger
from os import walk, remove

from src.settings_getter import get_settings_in_dict

@logger.catch
def search_valid_files_recursively(parent_directory):
    try:
        if not isinstance(parent_directory, str):
            raise TypeError(f"search_valid_files_recursively path passed as str is expected, not {type(parent_directory)}")
        file_names_list = list()
        valid_files_extensions = get_settings_in_dict["ALLOWED_INPUT_FILES_EXTENSIONS"]
        for (dirpath, dirnames, filenames) in walk(parent_directory):
            file_names_list.extend(filenames)
        valid_files_list = [filename for filename in file_names_list if get_extension(filename) in valid_files_extensions]
        return valid_files_list
    except Exception as e:
        logger.error(str(e))

@logger.catch
def get_extension(file_path):
    pass


def main():
    raise NotImplementedError("Use as package")

if __name__ == "__main__":
    main()