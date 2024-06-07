# Copyright (c) 2024 Jarid Prince

from days.day_046.files.helpers import *


def fetch_song_uri(song, year, sp):
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
        uri = result["tracks"]["items"][0]["uri"]
        return uri
    except (IndexError, KeyError):
        print(f'"{song}" doesn\'t exist in Spotify. Skipped.')
        return None


def day_046():
    title("SPOTIFY TIME MACHINE")
    load_dotenv()
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

    RDURI = "http://example.com"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=RDURI,
            scope="playlist-modify-private",
            show_dialog=True,
            cache_path="./tools/days/day_046/files/token.txt",
        )
    )
    user_id = sp.current_user()["id"]

    time_period = nli("What time would you like to travel to?\nFormat: YYYY-MM-DD")
    URL = f"https://www.billboard.com/charts/hot-100/{time_period}"

    response = requests.get(URL)
    # pprint(response)
    response.encoding = "utf-8"
    contents = response.text
    # pprint(contents)
    soup = BeautifulSoup(contents, "html.parser")

    # Find all li elements with class 'o-chart-results-list__item'
    list_items = soup.find_all("li", class_="o-chart-results-list__item")
    # Find all h3 elements within those li elements with the specific class and id
    song_titles = []
    for item in list_items:
        h3 = item.find("h3", class_="c-title", id="title-of-a-story")
        if h3:
            song_titles.append(h3.getText().strip())

    pprint(song_titles)

    song_uris = []
    year = time_period.split("-")[0]
    # introduced threading for speed to replace for song in song_titles:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_song = {
            executor.submit(fetch_song_uri, song, year, sp): song
            for song in song_titles
        }
        for future in concurrent.futures.as_completed(future_to_song):
            uri = future.result()
            if uri:
                song_uris.append(uri)
    pprint(song_uris)

    playlist = sp.user_playlist_create(
        user=user_id, name=f"{time_period} - Billboard 100", public=False
    )
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

    nls("Playlist successfully created! Check your spotify!")
    # print(song_titles)
    # print(user_id)
