# Copyright (c) 2024 Jarid Prince

from days.day_042.files.helpers import *


def day_042():
    title("BASIC HTML CV PRO")
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    try:
        this_directory = input(
            "Where is the Python100 Folder located?\ne.g. c:/Users/Bob/Downloads\nPress enter for default.\n"
        )
        if this_directory == "":
            this_directory = os.getcwd()
        print(f"Set directory location: {this_directory}")
        webbrowser.get(chrome_path).open(
            f"file://{this_directory}/tools/days/day_042/files/index.html"
        )
    except:
        try:
            webbrowser.get().open(
                "file://d:/dev/Python100/tools/days/day_042/files/index.html"
            )
        except:
            nls(
                "There is likely a problem with the file locations. You need to adjust the url location for your files."
            )
