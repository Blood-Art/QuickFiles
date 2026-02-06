import os

from pathlib import Path

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


def move_path(destination=Path(), path=Path(), is_augmented=True):

    where = ""
    if not is_augmented:
        path = input(" What do you want to move? or R to return : ")

        if str(path).lower() == "r":
            return 0

        where = input(f" Where do you want to move {path}? : ")

    if str(path)[0] == "~":
        home_sign = str(path).replace("~", str(home_dir))
        path = Path(home_sign)
        destination = f"{Path(where)}/{path.name}"

    if str(destination)[0] == "~":
        home_sign = str(destination).replace("~", str(home_dir))
        destination = Path(home_sign)

    destination_no_name = str(destination).rstrip(Path(path).name)
    try:
        Path(path).move(destination)
        print(f" {Path(path).name} was moved to {destination_no_name} succesfully!")

    except Exception as e:
        print(f" Couldn't Proceed {e}.")
