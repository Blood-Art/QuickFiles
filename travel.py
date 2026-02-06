import os

from pathlib import Path
import utils

home_dir = Path().home()


def go_home():
    if not home_dir.exists():
        print(" No home directory was found!")
        return 0

    return os.chdir(home_dir)


def change_dir(path=Path(), is_augmented=True):
    if not is_augmented:
        path = input(" Change to which path? or R to return : ")

    if str(path).lower() == "r":
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


def move_path(path=Path(), destination=Path(), is_augmented=True):

    where = ""

    if str(path)[0] == "~":
        home_sign = str(path).replace("~", str(home_dir))
        path = Path(home_sign)

    if str(destination)[0] == "~":
        home_sign = str(destination).replace("~", str(home_dir))
        destination = Path(home_sign)

    if not is_augmented:
        while True:
            path = input(" What do you want to move? or R to return : ")

            if path.lower() == "r":
                return 0

            elif not Path(path).exists():
                print(f" '{path}' does not exist")
                continue
            else:
                break

        while True:
            where = input(f" Where do you want to move '{path}'? : ")

            if not Path(where).exists():
                print(f" '{where}' does not exist")
                continue

            else:
                break
        destination = where

    destination_no_name = str(destination).replace(str(Path(path).name), "")

    try:
        destination = f"{destination}/{Path(path).name}"

        if Path(destination).exists():
            if Path(destination).is_file():
                utils.confirmation(destination)

            elif Path(destination).is_dir():
                print(
                    f" {Path(destination).name} already exists in {destination_no_name}."
                )
                return 0

        Path(path).move(destination)
        print(f" {Path(path).name} was moved to {destination_no_name} succesfully!")

    except FileNotFoundError:
        print(f" Path '{path}' not found.")

    except PermissionError:
        print(" You don't have permissions to move this path.")

    except Exception as e:
        print(f" Couldn't Proceed {e}.")
