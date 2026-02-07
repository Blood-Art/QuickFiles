from pathlib import Path

import utils

import os

import travel

import edit


home_path = Path().home()


def list_content(path=Path(), show_hidden=False):

    try:
        directory_content = path.iterdir()
        directory_list = []

        if not os.listdir(path):
            print(" There is nothing here.")
            return 0

        else:
            row_count = 0
            row_size = 4
            num_of_dashes = 90
            spacing = 20
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

                # starting a new line except if it's the last path in the list.
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

    except Exception as e:
        print(f" Couldn't proceed {e}")


def filter_input(
    choice: str, filtered_choice="", filtered_path="", filtered_destination=""
):
    inputs = choice.replace("~", str(home_path)).split(" ")

    if len(inputs) >= 1:
        filtered_choice = inputs[0]

    if len(inputs) >= 2:
        filtered_path = inputs[1]

    if len(inputs) >= 3:
        filtered_destination = inputs[2]

    if filtered_choice == str(home_path):
        filtered_choice = "~"

    return filtered_choice, Path(filtered_path), Path(filtered_destination)


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

    print(f" {'*' * 20} WELCOME {'*' * 20}")
    while is_on:
        currentpath = Path().absolute()
        print(f"\n Current path : [{currentpath}] 🧭")
        for key, value in options.items():
            print(f"\n {key} - {value}")

        choice = input("\n\n Choice : ")

        # Allow for dynamic options by combining the option with the path in the same line
        # Filter (Remove) all the numbers and spaces from the users choice

        filtered_choice, augmented_path, augmented_destination = filter_input(choice)

        if augmented_path:
            if not augmented_path.exists():
                print(f" '{augmented_path}' does not exist")

        if filtered_choice not in options.keys():
            print(f"'{filtered_choice}' is not a valid option.")
            continue

        utils.clear()

        try:
            choice = choice.replace("~", str(home_path))

            if choice == "1":
                travel.go_home()

            elif choice == f"2 {augmented_path}":
                list_content(augmented_path, show_hidden=True)

            elif choice == "2":
                list_content()

            elif choice == "5":
                edit.remove_path(is_augmented=False)

            elif choice == "6":
                edit.copy_path(is_augmented=False)

            elif choice == f"6 {augmented_path} {augmented_destination}":
                edit.copy_path(augmented_path, augmented_destination, is_augmented=True)

            elif choice == "7":
                travel.move_path(is_augmented=False)

            elif choice == f"7 {augmented_path} {augmented_destination}":
                travel.move_path(
                    augmented_path, augmented_destination, is_augmented=True
                )
            elif choice == "8":
                edit.edit_file(is_augmented=False)

            elif choice == f"8 {augmented_path}":
                edit.edit_file(augmented_path, is_augmented=True)

            elif choice == "9":
                print(" have a good day! 🫡")
                is_on = False

            elif choice == f"3 {augmented_path}":
                travel.change_dir(augmented_path, is_augmented=True)

            elif choice == "3":
                travel.change_dir(is_augmented=False)

            elif choice == f"4 {augmented_path}":
                edit.create_path(augmented_path, is_augmented=True)

            elif choice == "4":
                edit.create_path(is_augmented=False)

            elif choice == f"5 {augmented_path}":
                edit.remove_path(augmented_path, is_augmented=True)

            elif choice == f"5 {augmented_path}":
                edit.remove_path(augmented_path, is_augmented=True)

            else:
                if str(augmented_path) == str(home_path):
                    choice = choice.replace(str(home_path), "~")
                print(f" {choice} is not valid")

        except Exception as e:
            print(f" Couldn't proceed {e}")


def main():
    menu()


if __name__ == "__main__":
    main()
