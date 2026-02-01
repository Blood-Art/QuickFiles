import os

from pathlib import Path

home_dir = Path().home()


def go_home():
    if not home_dir.exists():
        print(" No home directory was found!")
        return 0

    return os.chdir(home_dir)


def change_dir(path=Path()):
    if path == Path():
        path = input(" Change to which path? or r to return : ")

    if path == "r":
        return 0

    if str(path)[0] == "~":
        home_sign = str(path).replace("~", str(home_dir))
        path = Path(home_sign)

    try:
        os.chdir(path)

    except FileExistsError:
        print(" File Doesn't Exist.")

    except FileNotFoundError:
        print(f" Path '{path}' not found.")

    except PermissionError:
        print(" You don't have permissions to enter this directory.")

    except NotADirectoryError:
        print(f"'{path}' is not a directory.")
