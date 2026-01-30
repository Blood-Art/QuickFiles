from os.path import isfile
from pathlib import Path

import os

import shutil


def createPath(path=Path(), type: str = ""):
    while True:
        type = input(" File or directory? (f/d) or r to return : ").lower()

        if type != "f" and type != "d" and type != "r":
            print(" Invalid input, f for file or d for directory")
            continue

        if type == "r":
            return 0

        if type == "f":
            # if there was no augmented path, ask for input
            if path == Path():
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
                print(f"\n path '{path}' hasn't been found.")

            except PermissionError:
                print(f"\n You don't have permission to create '{path}'")

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
                print(f"\n path '{path}' wasn't found.")

            except PermissionError:
                print(f"\n You don't have permission to create '{path}'")

        break


def removePath(fullpath=Path()):
    while True:
        name = ""
        if fullpath == Path():
            name = input(" Name of the file/directory? to remove or r to return : ")
            fullpath = Path(name).absolute()

        if name == "r".lower():
            return 0

        if str(fullpath)[0] == "~":
            homePath = Path().home()
            fullpath = Path(str(fullpath).replace("~", str(homePath)))

        if fullpath.exists():
            break

        else:
            print(f" path '{fullpath}' does not exist")
            return 0

    while True:
        confirmation = input(
            f" Are you sure? '{fullpath}' will be permanently removed (y/n) : "
        )

        if confirmation.lower() == "n":
            return 0

        elif confirmation.lower() == "y" or confirmation == "":
            try:
                if fullpath.is_dir():
                    shutil.rmtree(fullpath)
                    print(f" directory '{fullpath}' was removed succesfully!")

                elif fullpath.is_file():
                    os.remove(fullpath)
                    print(f" file '{fullpath}' was removed succesfully!")

                else:
                    print(" Error can't delete that.")

            except FileNotFoundError:
                print(f"\n path '{fullpath}' wasn't found.")

            except PermissionError:
                print(f" You don't have permission to remove '{fullpath}' here")

        else:
            print(
                f" '{confirmation}' is invalid, please enter y or enter for yes or n for no."
            )
            continue

        break


def copyPath(target=Path(), destination=Path()):
    while True:
        name = ""
        where = ""

        if target == Path():
            name = input(" Name of the file/directory to copy? or r to return : ")
            target = Path(name).absolute()

        if name.lower() == "r":
            return 0

        if target.exists():
            break

        else:
            print(f" '{target.name}' does not exist")
            target = Path()
            continue

    while True:
        home_replacement = ""
        destination_no_name = ""

        # there is no augmented path
        if destination == Path():
            where = input(f" Where do you want to copy '{target.name}' to? : ")
            destination_no_name = Path(where).absolute()
            destination = destination_no_name / target.name

        if where[0] == "~":
            home_path = Path().home()
            home_replacement = Path(where.replace("~", str(home_path)))
            destination_no_name = home_replacement
            destination = destination_no_name / target.name

        if not destination.parent.exists():
            print(f" '{destination_no_name}' does not exist.")
            destination = Path()
            continue

        if destination.is_file():
            while True:
                confirmation = input(
                    f"\n WARNING '{destination.name}' is a file, if you choose to continue {destination.name} will be overwritten are you sure? (y/n) : "
                )

                if confirmation.lower() == "y" or confirmation == "":
                    break

                elif confirmation.lower() == "n":
                    return 0

                else:
                    print(
                        f"\n '{confirmation}' is invalid, please enter y or enter for yes or n for no."
                    )
                    continue

        if Path(destination).exists() and not target.is_file():
            print(f"\n '{destination.name}' already exists in {destination_no_name}.")
            return 0

        try:
            if target.is_file():
                shutil.copy2(target, destination)

            elif target.is_dir():
                shutil.copytree(target, destination)
            print(
                f"'{target.name}' has been succesfully copied to {destination_no_name}! "
            )
            break

        except FileNotFoundError:
            print(f"\n path '{target}' wasn't found.")

        except NotADirectoryError:
            pass

        except PermissionError:
            print(
                f" You don't have permission to copy '{target.name}' into {destination}."
            )
