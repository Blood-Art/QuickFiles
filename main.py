from pathlib import Path

import subprocess

import os

import travel

import edit


def list_content(path=Path(), show_hidden=False):
    home_path = Path().home()

    if str(path)[0] == "~":
        new_home_path = Path(str(path).replace("~", str(home_path)))
        path = new_home_path

    try:
        directory_content = path.iterdir()
        directory_list = []

        if not os.listdir(path):
            print(" There is nothing here.")
            return 0

        else:
            row_count = 0
            row_size = 3
            num_of_dashes = 90
            spacing = 25
            for path in directory_content:
                if not show_hidden:
                    if path.name[0] != ".":
                        directory_list.append(path.name)

                else:
                    directory_list.append(path.name)

            directory_sorted = sorted(directory_list, key=str.lower)
            print(f" {'-' * num_of_dashes}")
            print(" " * spacing, end="")
            for sorted_path in directory_sorted:
                row_count += 1
                print(f" ({sorted_path})", end=" ")

                if row_count >= row_size and sorted_path != directory_sorted[-1]:
                    print()
                    print(" " * spacing, end="")
                    row_count = 0
            print(" " * spacing, end="")

        print(f"\n {'-' * 90}")

    except NotADirectoryError:
        print(f"'{path}' is not a directory.")

    except FileNotFoundError:
        print(f" Path '{path}' was not found.")

    except PermissionError:
        print(f" You don't have permission to list '{path}'.")


def filter_input(choice: str, filtered_choice=""):
    for char in choice:
        if char == " ":
            break

        else:
            filtered_choice += char

    filtered_path = choice[len(filtered_choice) + 1 : len(choice)]

    return filtered_choice, filtered_path


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

        filtered_choice = filter_input(choice)[0]

        filtered_path = filter_input(choice)[1]

        print(filtered_choice)

        print(filtered_path)

        augmented_path = Path(filtered_path)

        if filtered_choice not in options.keys():
            print(f"'{filtered_choice}' is not a valid option.")

            continue

        if choice == f"2 {augmented_path}":
            list_content(Path(augmented_path), show_hidden=True)

        elif choice == f"3 {augmented_path}":
            travel.change_dir(augmented_path)

        elif choice == f"4 {augmented_path}":
            edit.create_path(augmented_path)

        elif choice == f"5 {augmented_path}":
            edit.remove_path(augmented_path)

        if choice == "1":
            travel.go_home()

        elif choice == "2":
            list_content()

        elif choice == "3":
            travel.change_dir()

        elif choice == "4":
            edit.create_path()

        elif choice == "5":
            edit.remove_path()

        elif choice == "6":
            edit.copy_path()

        elif choice == "9":
            print(" have a good day! 🫡")
            is_on = False


def main():
    menu()


if __name__ == "__main__":
    main()
