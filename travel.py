import os

from os.path import exists
from pathlib import Path
import utils

home_path = Path().home()


def go_home():
    if not home_path.exists():
        print(" No home directory was found!")
        return 0

    return os.chdir(home_path)


def change_dir(path=Path(), is_augmented=True):
    if not is_augmented:
        path = input(" Change to which path? or R to return : ")

    if str(path).lower() == "r":
        utils.clear()
        return 0

    if str(path)[0] == "~":
        home_sign = str(path).replace("~", str(home_path))
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


def move_path(path=Path(), destination=Path(), is_augmented=True):

    while True:
        if not is_augmented:
            path = Path(
                input(" What do you want to move? or R to return: ").replace(
                    "~", str(home_path)
                )
            )

            if str(path).lower() == "r":
                utils.clear()
                return 0

        if not path.exists():
            print(f" '{path}' does not exist")
            continue

        else:
            break

    while True:
        if not is_augmented:
            destination = Path(
                input(f" Where do you want to move '{path}'? or R to return: ").replace(
                    "~", str(home_path)
                )
            )

        if str(destination).lower() == "r":
            utils.clear()
            return 0

        if not destination.exists():
            path.move(destination)
            break

        else:
            final_destination = destination / path.name
            path.move(final_destination)
            break
