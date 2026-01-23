from pathlib import Path

import os

import travel

import edit


def listContent(path=Path()):
    try:
        currDirContent = path.iterdir()

        if not os.listdir(path):
            print(" There is nothing here.")
            return 0

        else:
            for path in currDirContent:
                print(f" {path}", end=" ")

        print()

    except NotADirectoryError:
        print(f"'{path}' is not a directory")

    except FileNotFoundError:
        print(f" Path '{path}' was not found")


def menu():
    # listContent(Path("/usr/share/applications/"))
    options = {
        "1": "Go to home directory 🏠",
        "2": "List current working directory 🧰",
        "3": "Change directory 🏃",
        "4": "Create a file/directory 👷",
        "5": "Remove a file/directory 🙅‍♂️",
        "9": "Quit 🫡",
    }
    is_on = True

    while is_on:
        currentpath = Path().absolute()
        print(f"\n Current path : [{currentpath}] 🧭")
        for key, value in options.items():
            print(f"\n {key} - {value}")

        choice = input("\n Choice : ")

        # Allow for dynamic options by combining the option with the path in the same line
        # Filter (Remove) all the numbers and spaces from the users choice
        filterTable = str.maketrans("", "", "123456789 ")

        filteredChoice = choice.translate(filterTable)

        augmentedPath = Path(filteredChoice)

        # if choice not in options.keys():
        #     print(" Not a valid option.")
        #     print(f"{choice} {Path()}")
        #     # continue

        if choice == f"2 {augmentedPath}":
            listContent(Path(augmentedPath))

        elif choice == f"3 {augmentedPath}":
            travel.changeDir(augmentedPath)

        if choice == "1":
            travel.goHome()

        elif choice == "2":
            listContent()

        elif choice == "3":
            travel.changeDir()

        elif choice == "4":
            edit.createPath()

        elif choice == "5":
            edit.removePath()

        elif choice == "9":
            print(" have a good day!")
            is_on = False


def main():
    menu()


if __name__ == "__main__":
    main()
