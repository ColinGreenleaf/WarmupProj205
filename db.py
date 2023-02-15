import sqlite3

# Constants for Artist data
COUNTRY_FUNC = 2
TAGS_FUNC = 3
LISTENERS_FUNC = 4

# Constants for Song data
ARTIST_FUNC = 1
TITLE_FUNC = 2
GENRE_FUNC = 3
YEAR_FUNC = 4
ENERGY_FUNC = 5
DANCE_FUNC = 6
LOUD_FUNC = 7


### Single-Table Queries ###

# gets one element of data from a song
# param songName: the name of the song
# param function: the index of the data to be returned
def getDataOfSong(songName, function):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()
    # return row from songs table where songNametxt = songName
    c.execute("SELECT * FROM Songs WHERE songNametxt = ?", (songName,))
    song = c.fetchall()
    # get specified data from that row
    data = song[0][function]

    if c is not None:
        c.close()
    if conn is not None:
        conn.close()

    return data


# gets one element of data from an artist
# param artistName: the name of the artist
# param function: the index of the data to be returned
def getDataOfArtist(artistName, function):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()
    # return row from artists table where artistNametxt = artistName
    c.execute("SELECT * FROM Artists WHERE artistFpk = ?", (artistName,))
    artist = c.fetchall()
    # get specified data from that row
    data = artist[0][function]

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()

    return data


# gets all the songs from an artist
# param artist: the name of the artist
# returns a list of all the songs from the artist
def getAllSongsFromArtist(artist):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()
    # Returning all values from a table
    songs = c.execute("SELECT * FROM Songs WHERE artistFpk = ?", (artist,))
    songs = c.fetchall()

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()

    return songs


# gets all the information of a song
# param songName: the name of the song
# returns a list of the song's information
def getSong(songName):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Returning information from the artist table
    song = c.execute("SELECT * FROM Songs WHERE songNameTxt == ?", (songName,))
    song = c.fetchall()

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()

    return song


# gets all the information of an artist
# param artistName: the name of the artist
# returns a list of the artist's information
def getArtist(artistName):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Returning information from the artist table
    artist = c.execute("SELECT * FROM Artists WHERE artistFpk == ?", (artistName,))
    artist = c.fetchall()

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()

    return artist


### Metadata Queries ###

# method to get the number of artists in the database
# returns an int of the number of artists
def getAllArtists():
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Returning all values from a table
    artists = c.execute("SELECT * FROM Artists")
    artists = c.fetchall()
    artistNum = 0
    for i in artists:
        artistNum += 1

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()

    # Returning the number of artists
    return artistNum


# method to get the number of songs in the database
# returns an int of the number of songs
def getAllSongs():
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Returning all values from a table
    songs = c.execute("SELECT * FROM Songs")
    songs = c.fetchall()
    songNum = 0
    for i in songs:
        songNum += 1

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()
    # Returning the n
