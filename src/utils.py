from pathlib import Path

from subprocess import run

from os import name


def confirmation(destination):
    while True:
        destination_path = Path(destination)
        destination_no_name = destination.replace(str(destination_path.name), "")
        confirmation = input(
            f"\n WARNING '{destination_path.name}' exists in {destination_no_name}, if you choose to continue {destination_path.name} will be overwritten are you sure? (y/n) : "
        )

        if confirmation.lower() == "y" or confirmation == "":
            return True

        elif confirmation.lower() == "n":
            return False

        else:
            print(
                f"\n '{confirmation}' is invalid, please enter y or enter for yes or n for no."
            )
            continue


def clear():
    run("cls" if name == "nt" else "clear", shell=True)
