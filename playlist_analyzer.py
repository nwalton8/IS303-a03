'''
Noah Walton
IS303-A03

Playlist Analyzer
Analyzes a music playlist by duration and genre.

Inputs:
- Playlist name
- Music playlist (list of dictionaries with 'title', 'artist', 'duration', 'genre')

Processes:
- Accumulator: Calculate total playtime
- Min/Max: Find the longest song
- Filter: Filter songs by genre
- Accumulator: Count songs over/under a specified duration
- Transform: Clean the input data (strip spaces, title case)

Outputs:
- Name of Playlist with total playtime
- Longest song title and duration
- Count of songs over/under a specified duration
- List of songs and their details filtered by genre
'''
#Inputs:
playlist_name = input("Enter the name of the playlist: ").strip().title()
playlist = [
]
duration_threshold = int(input("Enter the duration threshold in seconds: "))
genre_filter = input("Enter a genre to filter by: ").strip().title()
add_song = ""
while add_song.strip().lower() != "done":
    title = input("Enter song title (or 'done' to finish): ").strip().title()
    if title.lower() == "done":
        break
    artist = input("Enter the artist's name: ").strip().title()
    duration = int(input("Enter the song duration in seconds: "))
    genre = input("Enter the song genre: ").strip().title()
    playlist.append({"title": title, "artist": artist, "duration": duration, "genre": genre})
if not playlist:
    print("No songs in the playlist.")
    exit()

#processes:
total_playtime = 0
longest_song = playlist[0]   # Initialize to the first song in the playlist
filtered_songs = [
]
over_threshold_count = 0
under_threshold_count = 0
for song in playlist:
    total_playtime += song['duration']
    if song['duration'] > longest_song['duration']:
        longest_song = song
    if song['genre'] == genre_filter:
        filtered_songs.append(song)
    if song['duration'] > duration_threshold:
        over_threshold_count += 1
    else:
        under_threshold_count += 1

#Outputs:
print(f"\nThe playlist, {playlist_name}, has a total playtime of {total_playtime} seconds.")
print(f"The longest song is '{longest_song['title']}' by {longest_song['artist']} with a duration of {longest_song['duration']} seconds.")
print(f"Number of songs over the threshold of {duration_threshold} seconds: {over_threshold_count}")
print(f"Number of songs under the threshold of {duration_threshold} seconds: {under_threshold_count}")
print(f"Filtered songs by genre '{genre_filter}':")
for song in filtered_songs:
    print(f"  - {song['title']} by {song['artist']} ({song['duration']} seconds)")

#End of playlist_analyzer.py