# Copyright (c) 2024 Jarid Prince

from days.day_045.files.helpers import *


def day_045():
    # response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
    # response.encoding="utf-8"
    # contents = response.text
    # EMPIRE MAG HAS BLOCKED LIVE SCRAPING WITH JS, SAVED RENDERED HTML TO FILE

    title("MUST WATCH LIST")
    with open("./tools/days/day_045/files/top100.html", encoding="utf-8") as website:
        contents = website.read()

    soup = BeautifulSoup(contents, "html.parser")

    titles_html = soup.find_all(name="h3", class_="jsx-4245974604")
    titles = [eachtitle.getText() for eachtitle in titles_html]
    ordered_titles = titles[::-1]
    formatted_list = "\n".join(ordered_titles)
    nls(formatted_list)

    with open("./tools/days/day_045/files/movies.txt", mode="w") as file:
        for movie in ordered_titles:
            file.write(f"{movie}\n")

    nls("Top 100 Movies saved to file 'movies.txt'.")
