# Copyright (c) 2024 Jarid Prince

import os
from misc import program_names

root_path = "./"
folders = []


def make_days_folder():
    os.mkdir(os.path.join(root_path, "days"))


def make_folders_and_py_files(start_num: int):
    num = start_num
    for folder in folders:
        os.mkdir(os.path.join(f"{root_path}/days", folder))
        new_root = f"./days/{folder}"
        os.mkdir(os.path.join(new_root, "files"))

        with open(os.path.join(new_root, "files", "helpers.py"), "w+") as helpers_file:
            helpers_file.write("from misc import nls, nli, title, cls, bcolors")

        with open(f"days/{folder}/main.py", "w+") as f:
            if (num + 1) < 10:
                func_title = "day_00" + str(num + 1)
            elif (num + 1) >= 10 and (num + 1) != 100:
                func_title = "day_0" + str(num + 1)
            else:
                func_title = "day_" + str(num + 1)

            f.write(
                f'from days.{folder}.files.helpers import *\n\ndef {func_title}():\n\ttitle("{program_names[num]}")'
            )
            f.close()
            print(program_names[num])
        num += 1


def run():
    # Checking if already have pre-existing folder (cases doing 10 days at a time for example)
    exists = input("\nDoes the folder for days already exist?\n'y' or 'n'\n")
    if exists == "n":
        make_days_folder()

    # Input validation
    legit = False
    while not legit:
        start_day = input(
            "\nWhat is the start day - type '1' for Day 1 onward, type '50' to create folders from day 50 on etc.\nValid options 1-100.\n"
        )
        try:
            start_day = int(start_day)
            if start_day < 1 or start_day > 100:
                print("start day is: ", start_day)
                legit = False
            else:
                legit = True
        except Exception as e:
            print(f"{e}\nInvalid input, try again!")

    # Create the files and folders
    for x in range(start_day, 101):
        if x < 10:
            folders.append("day_00" + str(x))
        elif x >= 10 and x != 100:
            folders.append("day_0" + str(x))
        else:
            folders.append("day_" + str(x))

    make_folders_and_py_files(start_num=start_day - 1)


run()
