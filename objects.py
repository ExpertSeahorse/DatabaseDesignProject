import subprocess
import datetime
class User:
    def __init__(self, name, passw, email, dob, country, kind, followers, following) -> None:
        self.name = name
        self.passw = passw
        # self.firstName = firstName
        # self.lastName = lastName
        self.email = email
        self.dob = dob
        self.country = country
        self.kind = kind
        self.followers = followers
        self.following = following
        self.playlists = [
            Playlist( "The best", songs[0:3]),
            Playlist( "The next", songs[2:5]),
            Playlist( "The third", songs[5:])
        ]

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

class Song:
    def __init__(self, name, artist=None, releaseDate=None, path=None) -> None:
        self.name = name
        self.artist = artist
        self.date = releaseDate
        self.path = path

    def play(self):
        subprocess.Popen(f" start /wait python .\MusicPlayer.py {self.name} {self.path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def match(self, query):
        return query.lower() in self.name.lower() or query.lower() in self.artist.lower()

    def __str__(self) -> str:
        return self.name + " " + self.artist
    

songs = [
    Song("Satisfaction", "The Rolling Stones", datetime.date(1965, 5, 1)), 
    Song("Imagine", "John Lennon", datetime.date(1971, 10, 1)), 
    Song("What's Going On", "Marvin Gaye", datetime.date(1971, 2, 1)),
    Song("Respect", "Aretha Franklin", datetime.date(1967, 4, 1)),
    Song("Good Vibrations", "The Beach Boys", datetime.date(1966, 10, 1)),
    Song("Johnny B. Goode", "Chuck Berry", datetime.date(1958, 4, 1)),
    Song("Hey Jude", "The Beatles", datetime.date(1968, 8, 1)),
    Song("Smells Like Teen Spirit", "Nirvana", datetime.date(1991, 9, 1)),
    Song("What'd I Say", "Ray Charles", datetime.date(1959, 6, 1))
]
# """
# We will eventually replace these with DB calls. Until then these help with designing the interface
# """
# import datetime
# class User:
#     def __init__(self, usern, passw, firstName, lastName, email, dob, country, following, followed_by, userType, playlistType, artistName, verified, favSongs, favArtists) -> None:
#         self.usern = usern
#         self.passw = passw
#         self.firstName = firstName
#         self.lastName = lastName
#         self.email = email
#         self.dob = dob
#         self.country = country
#         self.following = following
#         self.followed_by = followed_by

#         # not Guest
#         self.userType = userType
#         self.playlistType = playlistType

#         # Artist specific
#         self.artistName = artistName
#         self.verified = verified

#         # Premium specific
#         self.favSongs = favSongs
#         self.favArtists = favArtists

# userGuest = User(
#     "guest",
#     "pass",
#     "Guest",
#     "User",
#     "guest@test.com",
#     datetime.datetime.now(),
#     "Argentina",
#     ["James", "Adam"],
#     ["Adam", "Jules"],
#     "guest",
#     "", "", False, [], []
# )

# userPrem = User(
#     "premium",
#     "pass",
#     "Premium",
#     "User",
#     "premium@test.com",
#     datetime.datetime.now(),
#     "Egypt",
#     ["Mike"],
#     ["Adam", "George"],
#     "premium",
#     "playlist", "", False, ["Uptown Funk", "I Gotta Feeling"], ["Bruno Mars", "The Black Eyed Peas"]
# )

# userArtist = User(
#     "artist",
#     "pass",
#     "Artist",
#     "User",
#     "artist@test.com",
#     datetime.datetime.now(),
#     "United Kingdom",
#     [],
#     ["Otto", "Allison Downs", "Lily-Anne"],
#     "artist",
#     "album", "myArtistName", True, [], []
# )