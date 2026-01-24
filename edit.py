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
            name = input(" Name of the file/directory? or r to return : ")
            fullpath = Path(name).absolute()

        if name == "r".lower():
            return 0

        if fullpath.exists():
            pass

        else:
            print(f" path '{fullpath}' does not exist")
            return 0

        confirmation = input(
            f" Are you sure? '{fullpath}' will be permanently removed (y/n) : "
        )

        if confirmation.lower() == "n":
            return 0

        elif confirmation.lower() == "y" or confirmation == "\n":
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

        break
