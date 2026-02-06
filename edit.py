from pathlib import Path

import os

import shutil

import utils


home_path = Path().home()


def create_path(path=Path(), type: str = "", is_augmented=True):
    while True:
        if str(path) == "~":
            pass
        else:
            if str(path)[0] == "~":
                home_replacement = Path(str(path).replace("~", str(home_path)))
                path = home_replacement
        type = input(" File or directory? (F/D) or R to return : ").lower()

        if type != "f" and type != "d" and type != "r":
            print(" Invalid input, f for file or d for directory")
            continue

        if type == "r":
            return 0

        if type == "f":
            # if there was no augmented path, ask for input
            if not is_augmented:
                path = input(" Name of the file? : ")

            try:
                if Path(path).exists() and Path(path).is_file():
                    print(f" file '{path}' already exists")

                elif Path(path).exists() and Path(path).is_dir():
                    print(f" directory '{path}' already exists")

                else:
                    Path(path).touch()
                    print(f" file '{path}' was created succesfully!")

            except FileNotFoundError:
                print(f" path '{path}' hasn't been found.")
                return 0

            except PermissionError:
                print(f" You don't have permission to create '{path}'")
                return 0

        elif type == "d":
            # if there was no augmented path, ask for input
            if path == Path():
                path = input(" Name of the directory? : ")

            try:
                if Path(path).exists() and Path(path).is_file():
                    print(f" file '{path}' already exists")

                elif Path(path).exists() and Path(path).is_dir():
                    print(f" directory '{path}' already exists")

                else:
                    Path(path).mkdir()
                    print(f" directory '{path}' was created succesfully!")

            except FileNotFoundError:
                print(f" path '{path}' wasn't found.")
                return 0

            except PermissionError:
                print(f" You don't have permission to create '{path}'")
                return 0

        break


def remove_path(full_path=Path(), is_augmented=True):
    while True:
        name = ""
        if not is_augmented:
            name = input(" Name of the file/directory? to remove or R to return : ")
            full_path = Path(name).absolute()

        if name.lower() == "r":
            return 0

        # Pass if ~ exists in the current direco
        if str(full_path) == "~":
            pass

        else:
            if str(full_path)[0] == "~":
                full_path = Path(str(full_path).replace("~", str(home_path)))

        if full_path.exists():
            break

        else:
            print(f" path '{full_path}' does not exist")
            return 0

    while True:
        confirmation = input(
            f" Are you sure? '{full_path}' will be permanently removed (y/n) : "
        )

        if confirmation.lower() == "n":
            return 0

        elif confirmation.lower() == "y" or confirmation == "":
            try:
                if full_path.is_dir():
                    shutil.rmtree(full_path)
                    print(f" directory '{full_path}' was removed succesfully!")

                elif full_path.is_file():
                    os.remove(full_path)
                    print(f" file '{full_path}' was removed succesfully!")

                else:
                    print(" Error can't delete that.")

            except FileNotFoundError:
                print(f" path '{full_path}' wasn't found.")
                return 0

            except PermissionError:
                print(f" You don't have permission to remove '{full_path}' here")
                return 0

        else:
            print(
                f" '{confirmation}' is invalid, please enter y or enter for yes or n for no."
            )
            continue

        break


def copy_path(target=Path(), destination=Path(), is_augmented=True):

    while True:
        if not is_augmented:
            target = Path(input(" Which file to copy? or R to return : "))

            if str(target).lower() == "r":
                return 0

        if str(target)[0] == "~":
            target = str(target).replace("~", str(Path().home()))

        if not Path(target).exists():
            print(f" '{target}' does not exist.")
            continue

        else:
            break

    while True:
        if not is_augmented:
            destination = Path(
                input(f" Where do you to copy '{target}' to? or R to return : ")
            )

            if str(destination).lower() == "r":
                return 0

        if str(destination)[0] == "~":
            destination = str(destination).replace("~", str(Path().home()))

        if not Path(destination).exists():
            print(f" '{destination}' does not exist")
            continue

        else:
            break

    try:
        target = Path(target)
        destination = Path(destination)
        final_destination = f"{destination}/{target.name}"
        if Path(target).is_file():
            shutil.copy2(target, final_destination)

        elif Path(target).is_dir():
            shutil.copytree(target, final_destination)

        print(f"'{target.name}' has been succesfully copied to {destination}!")

    except Exception as e:
        print(f" Couldn't Proceed {e}.")
