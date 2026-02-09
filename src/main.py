from pathlib import Path

import utils

import os

import travel

import edit


home_path = Path().home()


def list_content(*path_list, show_hidden=False, is_augmented=True):

    if not is_augmented:
        path_list = (Path(),)

    for p in path_list:
        if p != "":
            if str(p) != ".":
                print(f"\n {p}")

            try:
                p = Path(p)
                directory_content = p.iterdir()
                directory_list = []

                if not os.listdir(p):
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
                        if (
                            row_count >= row_size
                            and sorted_path != directory_sorted[-1]
                        ):
                            print()
                            print(" " * spacing, end="")
                            row_count = 0
                    print(" " * spacing, end="")

                print(f"\n {'-' * 90}")

            except NotADirectoryError:
                print(f"'{p}' is not a directory.")

            except FileNotFoundError:
                print(f" Path '{p}' was not found.")

            except PermissionError:
                print(f" You don't have permission to list '{p}'.")

            except Exception as e:
                print(f" Couldn't proceed {e}")


def filter_input(
    choice: str, filtered_choice="", filtered_path_list="", filtered_destination=""
):
    inputs = choice.replace("~", str(home_path)).split(" ")

    if len(inputs) >= 1:
        filtered_choice = inputs[0]

    if len(inputs) >= 2:
        filtered_path_list = inputs[1 : len(inputs)]

    if len(inputs) >= 3:
        filtered_destination = inputs[-1]

    if filtered_choice == str(home_path):
        filtered_choice = "~"

    return filtered_choice, filtered_path_list, Path(filtered_destination)


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

    utils.clear()
    print(f" {'*' * 20} WELCOME {'*' * 20}")
    while is_on:
        currentpath = Path().absolute()
        print(f"\n Current path : [{currentpath}] 🧭")
        for key, value in options.items():
            print(f"\n {key} - {value}")

        choice = input("\n\n Choice : ")

        # Allow for dynamic options by combining the option with the path in the same line
        # Filter (Remove) all the numbers and spaces from the users choice

        filtered_choice, augmented_path_list, augmented_destination = filter_input(
            choice
        )

        paths_string = " ".join(augmented_path_list)

        if filtered_choice not in options.keys():
            utils.clear()
            print(f"'{filtered_choice}' is not a valid option.")
            continue

        utils.clear()

        try:
            choice = choice.replace("~", str(home_path))

            if choice == "1":
                travel.go_home()

            elif choice == "2 .":
                list_content(show_hidden=True, is_augmented=False)

            elif choice == f"2 {paths_string}":
                list_content(*augmented_path_list, show_hidden=False, is_augmented=True)

            elif choice == "2":
                list_content(show_hidden=False, is_augmented=False)

            elif choice == f"3 {paths_string}":
                travel.change_dir(Path(augmented_path_list[0]), is_augmented=True)

            elif choice == "3":
                travel.change_dir(is_augmented=False)

            elif choice == f"4 {paths_string}":
                edit.create_path(*augmented_path_list, is_augmented=True)

            elif choice == "4":
                edit.create_path(is_augmented=False)

            elif choice == f"5 {paths_string}":
                edit.remove_path(*augmented_path_list, is_augmented=True)

            elif choice == "5":
                edit.remove_path(is_augmented=False)

            elif choice == f"6 {paths_string}":
                edit.copy_path(
                    *augmented_path_list,
                    augmented_destination,
                    is_augmented=True,
                )
            elif choice == "6":
                edit.copy_path(is_augmented=False)

            elif choice == f"7 {paths_string}":
                travel.move_path(
                    *augmented_path_list, augmented_destination, is_augmented=True
                )
            elif choice == "7":
                travel.move_path(is_augmented=False)

            elif choice == "8":
                edit.edit_file(is_augmented=False)

            elif choice == f"8 {paths_string}":
                edit.edit_file(Path(augmented_path_list[0]), is_augmented=True)

            elif choice == "9":
                print(" have a good day! 🫡")
                is_on = False

            else:
                if str(augmented_path_list) == str(home_path):
                    choice = choice.replace(str(home_path), "~")
                print(f" {choice} is not valid")

        except Exception as e:
            print(f" Couldn't proceed {e}")


def main():
    menu()


if __name__ == "__main__":
    main()
