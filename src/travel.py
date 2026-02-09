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


def move_path(*paths, destination=Path(), is_augmented=True):

    if not is_augmented:
        while True:
            path = input(" What do you want to move? or R to return: ").replace(
                "~", str(home_path)
            )

            if path.lower() == "r":
                utils.clear()
                return 0

            paths_to_move = path.split(" ")

            paths = paths_to_move

            break

        while True:
            destination = input(
                f" Where do you want to move '{path}'? or R to return: "
            ).replace("~", str(home_path))

            if destination.lower() == "r":
                utils.clear()
                return 0

            break

    if is_augmented:
        destination = paths[-1]
        paths = paths[0:-2]

    path_list = []
    for p in paths:
        try:
            path_list.append(p)
            p = Path(p)
            destination = Path(destination)
            if not p.exists():
                print(f" '{p}' does not exist.")

            final_destination = destination / p.name

            if not p.exists():
                print(f" '{p}' does not exist.")

            if not destination.exists():
                p.move(destination)
                print(f" {p.name} has been renamed to '{destination}' succesfully!")

            else:
                p.move(final_destination)

        except NotADirectoryError:
            print(f" '{destination}' is not a directory, you can't move '{p}' to it.")

        except Exception as e:
            print(f" Couldn't proceed {e}")

    print(f" '{', '.join(path_list)}' has been moved to {destination} succesfully!")
