from loguru import logger
from os import walk, remove

from src.settings_getter import get_settings_in_dict


@logger.catch
def search_valid_files_recursively(parent_directory):
    try:
        if not isinstance(parent_directory, str):
            raise TypeError(
                f"search_valid_files_recursively path passed as str is expected, not {type(parent_directory)}"
            )
        valid_files_extensions = get_settings_in_dict()[
            "ALLOWED_INPUT_FILES_EXTENSIONS"
        ]

        if is_file(parent_directory):
            filename = parent_directory
            if not get_extension(filename) in valid_files_extensions:
                return
            return filename

        file_names_list = list()
        for (dirpath, dirnames, filenames) in walk(parent_directory):
            file_names_list.extend(filenames)
        valid_files_list = [
            filename
            for filename in file_names_list
            if get_extension(filename) in valid_files_extensions
        ]
        return valid_files_list
    except Exception as e:
        logger.error(str(e))


@logger.catch
def is_file(path):
    pass


@logger.catch
def get_extension(file_path):
    NO_SLASH_FOUND = -1
    NO_DOT_FOUND = -1
    if not isinstance(file_path, str):
        raise TypeError(f"get_extension: string input expected, not {type(file_path)}")
    last_slash_index = file_path.rfind("/")
    if last_slash_index != NO_SLASH_FOUND:
        file_path = file_path[last_slash_index:]
    dot_index = file_path.rfind(".")
    if dot_index == NO_DOT_FOUND:
        return None
    return file_path[dot_index:]


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
