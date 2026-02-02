from pathlib import Path

import os

import shutil


home_path = Path().home()


def create_path(path=Path(), type: str = ""):
    while True:
        if str(path)[0] == "~":
            home_replacement = Path(str(path).replace("~", str(home_path)))
            path = home_replacement
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


def remove_path(full_path=Path(), is_augmented=True):
    while True:
        name = ""
        if not is_augmented:
            name = input(" Name of the file/directory? to remove or r to return : ")
            full_path = Path(name).absolute()

        if name == "r".lower():
            return 0

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
                print(f"\n path '{full_path}' wasn't found.")

            except PermissionError:
                print(f" You don't have permission to remove '{full_path}' here")

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

        # if not Path(where).exists():
        #     destination = Path()
        #     continue

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
