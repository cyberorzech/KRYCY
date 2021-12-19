import inspect
from loguru import logger

from src.files_management.files import File


class TXT_File(File):
    def __init__(cls, path) -> None:
        super().__init__()
        cls.EXTENSION = ".txt"
        cls.path = path

    def read(cls) -> list:
        try:
            if cls.check_extension(cls.EXTENSION, cls.path) == False:
                raise ValueError(f"{inspect.currentframe().f_code.co_name}: invalid file extension. Expects {cls.EXTENSION}, got {path} instead")
            with open(cls.path) as f:
                txt_line_by_line = f.readlines()
            return txt_line_by_line
        except Exception as e:
            logger.error(str(e))

def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
