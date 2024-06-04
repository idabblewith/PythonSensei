# Copyright (c) 2024 Jarid Prince
# Used to mass create directories required files.

import os

root_path = "./"
folders = []


for x in range(26, 101):
    if x < 10:
        folders.append("day_00" + str(x))
    elif x >= 10 and x != 100:
        folders.append("day_0" + str(x))
    else:
        folders.append("day_" + str(x))


for folder in folders:
    directory = "./tools/days/"
    path = os.path.join(directory, folder)
    filespath = os.path.join(directory, f"{folder}/files")
    os.mkdir(path)
    print(f"Directory created: {directory}{path}")
    os.mkdir(filespath)
    print(f"Directory created: {directory}{filespath}")
    helper = f"./tools/days/{folder}/files/helpers.py"
    with open(helper, "w+") as h:
        h.write(f"from misc import nls, nli, title, cls")

    start = f"./tools/days/{folder}/main.py"
    with open(start, "a+") as f:
        f.write(f"from days.{folder}.files.helpers import *\n\ndef {folder}():\n\tpass")

# import_list = [f'from days.{folder}.main import {folder}\n' for folder in folders]
# function_list = [f'{folder}' for folder in folders]
# pylaunch = './tools/ProgramLauncher.py'
# for item in import_list:
#     with open(pylaunch, 'a+') as f:
#         f.write(item)
# with open(pylaunch, 'a+') as f:
#         f.write('[')
# for item in function_list:
#     with open(pylaunch, 'a+') as f:
#         f.write(f'{item}, ')
# with open(pylaunch, 'a+') as f:
#         f.write(']')
