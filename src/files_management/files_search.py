from loguru import logger

@logger.catch
def search_valid_files_recursively(parent_directory):
    try:
        if not isinstance(parent_directory, str):
            raise TypeError(f"search_valid_files_recursively path passed as str is expected, not {type(parent_directory)}")
        
    except Exception as e:
        logger.error(str(e))


def main():
    raise NotImplementedError("Use as package")

if __name__ == "__main__":
    main()