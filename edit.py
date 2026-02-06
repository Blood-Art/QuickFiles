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
        name = ""
        where = ""

        if not is_augmented:
            name = input(" Name of the file/directory to copy? or r to return : ")
            target = Path(name).absolute()

        if name.lower() == "r":
            return 0

        if target.exists():
            break

        elif target != Path():
            print(f" '{target.name}' does not exist")
            target = Path()
            continue

    while True:
        home_replacement = ""
        destination_no_name = ""

        # there is no augmented path
        if destination == Path():
            where = input(f" Where do you want to copy '{target.name}' to? : ")

            if where[0] == "~":
                destination_no_name = Path(where.replace("~", str(home_path)))
            else:
                destination_no_name = Path(where).absolute()

            destination = destination_no_name / target.name

        if str(destination)[0] == "~":
            home_sign = str(destination).replace("~", str(home_path))
            home_replacement = Path(home_sign)
            destination_no_name = home_replacement
            destination = destination_no_name / target.name

        if not destination.parent.exists():
            print(f" '{destination_no_name}' does not exist.")
            destination = Path()
            continue

        if destination.is_file():
            utils.confirmation(destination)

        if Path(destination).exists() and not target.is_file():
            print(f" '{destination.name}' already exists in {destination_no_name}.")
            return 0

        try:
            if target.is_file():
                shutil.copy2(target, destination)

            elif target.is_dir():
                shutil.copytree(target, destination)
            print(f"'{target.name}' was copied to {destination_no_name} succesfully!")
            break

        except FileNotFoundError:
            print(f" path '{target}' wasn't found.")
            return 0

        except NotADirectoryError:
            return 0

        except PermissionError:
            print(
                f" You don't have permission to copy '{target.name}' into {destination}."
            )
            return 0
