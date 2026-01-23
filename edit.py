from pathlib import Path

import os

import shutil


def createPath(name=Path(), type: str = ""):
    while True:
        type = input(" File or directory? (f/d) or r to return : ").lower()

        if type != "f" and type != "d" and type != "r":
            print(" Invalid input, f for file or d for directory")
            continue

        if type == "r":
            return 0

        if type == "f":
            name = input(" Name of the file? : ")

            if Path(name).exists():
                print("\n file '{name}' already exists.")

            else:
                Path(name).touch()
                print(f" file '{name}' was created succesfully!")

        elif type == "d":
            name = input(" Name of the directory? : ")

            try:
                Path(name).mkdir()
                print(f" directory '{name}' was created succesfully!")

            except FileExistsError:
                print("\n directory with that name already exists.")

            except PermissionError:
                print(f"\n You don't have permission to create '{name}'")

        break


def removePath(path=Path()):
    while True:
        name = input("Name of the file/directory? or r to return : ")
        fullpath = Path(name).absolute()

        if name == "r".lower():
            return 0

        if fullpath.exists():
            try:
                if fullpath.is_dir():
                    shutil.rmtree(fullpath)
                    print(f" directory '{name}' was removed succesfully!")

                elif fullpath.is_file():
                    os.remove(fullpath)
                    print(f" file '{name}' was removed succesfully!")

                else:
                    print(" Error can't delete that")

            except PermissionError:
                print(f" You don't have permission to create '{name}' here")

        else:
            print(f"'{name}' does not exist")

        break
