# Start with your program from (album).
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input
# and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.

album_details = {}

entries_count = 0
def make_album(artist_name, album_name, track_count = ''):
    if track_count:
        album_details['Artist'] = artist_name
        album_details['Album'] = album_name
        album_details['Tracks'] = track_count

    else:
        album_details['Artist'] = artist_name
        album_details['Album'] = album_name

    print(album_details)

while True:
    entries_count += 1

    artist = input("\nEnter an artist's name.: \n")
    album = input("Enter the album's name.: \n")
    tracks = input('\nEnter the number of tracks.: \n')
    

    if entries_count == 4:
        break

make_album(artist, album, tracks)