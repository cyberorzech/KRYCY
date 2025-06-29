import sys
import json


def get_settings_in_dict():
    try:
        with open("settings.json") as f:
            settings = json.load(f)
            f.close()
        return settings
    except Exception as e:
        sys.exit("Exception occured: " + str(e))


def main():
    raise NotImplementedError("Use as package")


if __name__ == "__main__":
    main()
