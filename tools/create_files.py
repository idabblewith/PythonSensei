# Copyright (c) 2024 Jarid Prince

import os
from misc import program_names

root_path = "./"
folders = []

for x in range(1, 101):
    if x < 10:
        folders.append("day_00" + str(x))
    elif x >= 10 and x != 100:
        folders.append("day_0" + str(x))
    else:
        folders.append("day_" + str(x))


def make_days_folder():
    os.mkdir(os.path.join(root_path, "days"))


def make_folders_and_py_files():
    num = 0
    for folder in folders:
        os.mkdir(os.path.join(f"{root_path}/days", folder))
        new_root = f"./days/{folder}"
        os.mkdir(os.path.join(new_root, "files"))
        with open(f"days/{folder}/main.py", "w+") as f:
            f.write(
                f'from tools.misc import *\nfrom days.{folder}.files import *\n\ndef day{num+1}():\n\ttitle("{program_names[num]}")'
            )
            f.close()
            print(program_names[num])
        num += 1


def run():
    make_days_folder()
    make_folders_and_py_files()


run()
