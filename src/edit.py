from pathlib import Path

import os

import shutil

import subprocess

import utils


home_path = Path().home()


def create_path(*path_list, type: str = "", is_augmented=True):

    if not is_augmented:
        path_name = input(" Name of the file/directory? : ").replace(
            "~", str(home_path)
        )
        paths = path_name.split()

        for p in paths:
            if p != " ":
                path_list = list(path_list)
                path_list.append(p)

    for path in path_list:
        while True:
            if path == home_path:
                path = str(path).replace(str(home_path), "~")

            type = input(
                f" File or directory? (F/D) for '{path}' or R to return : "
            ).lower()

            if type != "f" and type != "d" and type != "r":
                print(" Invalid input, f for file or d for directory")
                continue

            if type == "r":
                return 0

            if type == "f":
                # if there was no augmented path, ask for input

                try:
                    if Path(path).exists() and Path(path).is_file():
                        print(f" File '{path}' already exists.")

                    elif Path(path).exists() and Path(path).is_dir():
                        print(f" Directory '{path}' already exists.")

                    else:
                        Path(path).touch()
                        print(f" File '{path}' was created succesfully!")

                except FileNotFoundError:
                    print(f" Path '{path}' hasn't been found.")
                    return 0

                except PermissionError:
                    print(f" You don't have permission to create '{path}'.")
                    return 0

            elif type == "d":
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


def remove_path(*full_paths, is_augmented=True):

    if not is_augmented:
        while True:
            name = ""
            name = input(
                " Name of the file/directory? to remove or R to return : "
            ).replace("~", str(home_path))

            if name.lower() == "r":
                utils.clear()
                return 0

            paths = name.split(" ")

            full_paths = paths

            break

    for p in full_paths:
        while True:
            confirmation = input(
                f" Are you sure? '{p}' will be permanently removed (y/n) : "
            )

            if confirmation.lower() == "n":
                return 0

            elif confirmation.lower() == "y" or confirmation == "":
                try:
                    p = Path(p)
                    if p.is_dir():
                        shutil.rmtree(p)
                        print(f" directory '{p}' was removed succesfully!")

                    elif p.is_file():
                        os.remove(p)
                        print(f" file '{p}' was removed succesfully!")

                    else:
                        print(" Error can't delete that.")

                except FileNotFoundError:
                    print(f" path '{p}' wasn't found.")
                    return 0

                except PermissionError:
                    print(f" You don't have permission to remove '{p}' here")
                    return 0

            else:
                print(
                    f" '{confirmation}' is invalid, please enter y or enter for yes or n for no."
                )
                continue

            break


def copy_path(*targets, destination=Path(), is_augmented=True):

    target_input = ""
    if not is_augmented:
        while True:
            target_input = input(" What do you want to copy? or R to return : ")

            if target_input.lower() == "r":
                return 0

            targets = target_input.split(" ")

            break

        while True:
            destination = input(
                f" Where do you want to copy {targets}? or R to return : "
            ).replace("~", str(home_path))

            if target_input.lower() == "r":
                return 0

            break

    if is_augmented:
        destination = targets[-1]
        targets = list(targets[0:-2])

    if not Path(destination).exists():
        print(f" '{destination}' does not exist.")
        return 0

    for target in targets:
        if not Path(target).exists():
            print(f" '{target}' does not exist.")

        elif target != "":
            final_destination = Path(destination) / f"{target}"
            try:
                if (
                    Path(final_destination).exists()
                    and Path(final_destination).is_file()
                ):
                    utils.confirmation(str(final_destination))
                if Path(target).is_file():
                    shutil.copy2(target, final_destination)
                    print(f" File '{target}' was copied to {destination} succesfully!")

                elif Path(target).is_dir():
                    shutil.copytree(target, final_destination)
                    print(
                        f" Directory '{target}' was copied to {destination} succesfully!"
                    )
            except Exception as e:
                print(f" Couldn't Proceed {e}")


def edit_file(target=Path(), text_editor="", is_augmented=True):

    config_file = ".file_manager.conf"

    config_path = Path().home() / config_file

    supported_editors = ("nano", "vim", "nvim")

    if not config_path.exists():
        while True:
            text_editor = input(" What is your favourite text editor? : ").lower()

            if text_editor not in supported_editors:
                print(f" Sorry only {supported_editors} are supported.")
                continue

            else:
                break

        with open(config_path, "w") as file:
            file.write(text_editor)

    else:
        with open(config_path, "r") as file:
            text_editor = file.read()

    while True:
        if not is_augmented:
            target = Path(
                input(" Which file do you want to edit? or R to return : ").replace(
                    "~", str(home_path)
                )
            )

            if str(target).lower() == "r":
                utils.clear()
                return 0

        if not Path(target).exists() or target == "":
            print(f" '{target}' does not exist")
            is_augmented = False
            continue

        else:
            break
    run_editor = f"{text_editor} {Path(target)}"
    subprocess.run(
        run_editor,
        shell=True,
    )
    print(f" '{target}' has been edited succesfully!")
