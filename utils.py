from pathlib import Path


def confirmation(destination):
    while True:
        destination_no_name = destination.replace(str(Path(destination).name), "")
        confirmation = input(
            f"\n WARNING '{Path(destination).name}' exists in {destination_no_name}, if you choose to continue {Path(destination).name} will be overwritten are you sure? (y/n) : "
        )

        if confirmation.lower() == "y" or confirmation == "":
            return confirmation

        elif confirmation.lower() == "n":
            return 0

        else:
            print(
                f"\n '{confirmation}' is invalid, please enter y or enter for yes or n for no."
            )
            continue
