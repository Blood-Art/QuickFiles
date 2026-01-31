import os

from pathlib import Path


def go_home(homeDir=Path().home()):
    if not homeDir.exists():
        print(" No home directory was found!")
        return 0

    return os.chdir(homeDir)


def change_dir(path=Path()):
    if path == Path():
        path = input(" Change to which path? or r to return : ")

    if path == "r":
        return 0

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
