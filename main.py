from pathlib import Path

import subprocess

import os

import travel

import edit


def listContent(path=Path()):
    try:
        currDirContent = path.iterdir()
        currDirList = []
        if not os.listdir(path):
            print(" There is nothing here.")
            return 0

        else:
            row_count = 0
            row_size = 5
            for path in currDirContent:
                currDirList.append(path.name)

            currDirSortedList = sorted(currDirList, key=str.lower)
            print(f" {'-' * 90}")
            for sortedPath in currDirSortedList:
                row_count += 1
                print(f" ({sortedPath})", end=" ")

                if row_count >= row_size and sortedPath != currDirSortedList[-1]:
                    print()
                    row_count = 0

        print(f"\n {'-' * 90}")

    except NotADirectoryError:
        print(f"'{path}' is not a directory.")

    except FileNotFoundError:
        print(f" Path '{path}' was not found.")

    except PermissionError:
        print(f" You don't have permission to list '{path}'.")


def menu():
    options = {
        "1": "Go to home directory 🏠",
        "2": "List current working directory 🧰",
        "3": "Change directory 🏃",
        "4": "Create a file/directory 👷",
        "5": "Remove a file/directory ❌",
        "6": "Copy a file/directory 🌀",
        "7": "Move a file/directory 🔄",
        "8": "Edit a file 👨‍🔧",
        "9": "Quit 🚪",
    }
    is_on = True

    while is_on:
        currentpath = Path().absolute()
        print(f"\n Current path : [{currentpath}] 🧭")
        for key, value in options.items():
            print(f"\n {key} - {value}")

        choice = input("\n\n Choice : ")

        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

        # Allow for dynamic options by combining the option with the path in the same line
        # Filter (Remove) all the numbers and spaces from the users choice
        filteredPathTable = str.maketrans("", "", "123456789 ")

        filteredPath = choice.translate(filteredPathTable)

        filteredChoice = "".join(filter(str.isdigit, choice))

        augmentedPath = Path(filteredPath)

        if filteredChoice not in options.keys():
            print(" Not a valid option.")
            continue

        if choice == f"2 {augmentedPath}":
            listContent(Path(augmentedPath))

        elif choice == f"3 {augmentedPath}":
            travel.changeDir(augmentedPath)

        elif choice == f"4 {augmentedPath}":
            edit.createPath(augmentedPath)

        elif choice == f"5 {augmentedPath}":
            edit.removePath(augmentedPath)

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

        elif choice == "6":
            edit.copyPath()

        elif choice == "9":
            print(" have a good day! 🫡")
            is_on = False


def main():
    menu()


if __name__ == "__main__":
    main()
