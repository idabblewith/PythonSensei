# Copyright (c) 2022 Jarid Prince

from days.day_046.files.helpers import *

def day_046():
	title("SPOTIFY TIME MACHINE")
	with open("./tools/secrets/spotify_client_id.secret") as cid:
		CID = cid.read()
	with open("./tools/secrets/spotify_client_secret.secret") as csec:
		CSEC = csec.read()
	RDURI = "http://example.com"

	sp = spotipy.Spotify(
		auth_manager=SpotifyOAuth(
			client_id=CID, 
			client_secret=CSEC, 
			redirect_uri=RDURI, 
			scope="playlist-modify-private",
			show_dialog=True,
			cache_path="./tools/days/day_046/files/token.txt"
			)
		)
	user_id = sp.current_user()["id"]

	time_period = nli("What time would you like to travel to?\nFormat: YYYY-MM-DD")
	URL = f"https://www.billboard.com/charts/hot-100/{time_period}"

	response = requests.get(URL)
	response.encoding="utf-8"
	contents = response.text
	soup = BeautifulSoup(contents, "html.parser")

	songs_raw = soup.find_all(name='span', class_="chart-element__information__song")
	song_titles = [song.getText() for song in songs_raw]

	song_uris = []
	year = time_period.split("-")[0]
	for song in song_titles:
		result = sp.search(q=f'track:{song} year:{year}', type='track', limit=1)
		# print(result)
		try:
			uri = result['tracks']['items'][0]['uri']
			song_uris.append(uri)
		except(IndexError):
			print(f'"{song}" doesn\'t exist in Spotify. Skipped.')
	pprint(song_uris)

	playlist = sp.user_playlist_create(user=user_id, name=f'{time_period} - Billboard 100', public=False)
	sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

	nls("Playlist successfully created! Check your spotify!")
	# print(song_titles)
	# print(user_id)