# Copyright (c) 2024 Jarid Prince

from days.day_041.files.helpers import *


def day_041():
    title("BASIC HTML CV")
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    try:
        this_directory = input(
            "Where is the Python100 Folder located?\ne.g. c:/Users/Bob/Downloads\nPress enter for default location.\n"
        )
        if this_directory == "":
            this_directory = os.getcwd()
        print(f"Set directory location: {this_directory}")
        webbrowser.get(chrome_path).open(
            f"file://{this_directory}/tools/days/day_041/files/index.html"
        )
    except:
        nls(
            f"There is likely a problem with the file locations. You need to adjust the url location for your files.\nThe directory you have set is {this_directory}"
        )
