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


def getAllSongsFromArtist(artist):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()
    # Returning all values from a table
    print("\nAll " + artist + " songs:\n")
    songs = c.execute("SELECT * FROM Songs WHERE artistFpk = ?", (artist,))
    songs = c.fetchall()
    # print each song with no brackets
    for i in songs:
        print(str(i).replace(")", "").replace("(", ""))
    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()


### Utility Functions ###

# cleans up the print statements
def cleanPrint(value):
    returnVal = str(value).replace(")", "").replace("(", "").replace("[", "").replace("]", "").replace("'", "")
    return returnVal


### Single-Table Queries ###

# gets one element of data from a song, denoted by the function parameter
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

# gets one element of data from an artist, denoted by the function parameter
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

# gets all the information of a song
def getSong(songName):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Returning information from the artist table
    print("\nAll of the information on the song " + songName + ":\n")
    song = c.execute("SELECT * FROM Songs WHERE songNameTxt == ?", (songName,))
    song = c.fetchall()

    # Separating the values into a list and outputting
    songList = str(song).split(",")
    print("#" + cleanPrint(songList[0]) + "." + cleanPrint(songList[2]) + ", by " + cleanPrint(songList[1]))
    print("Genre:" + cleanPrint(songList[3]) + ". Released in" + cleanPrint(songList[4]))
    print("Energy:" + cleanPrint(
        songList[6] + " --- Danceability:" + cleanPrint(songList[7])) + " --- Loudness: " + cleanPrint(songList[7]))

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()


# gets all the information of an artist
def getArtist(artistName):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Returning information from the artist table
    print("\nAll of the information on " + artistName + ":\n")
    artist = c.execute("SELECT * FROM Artists WHERE artistFpk == ?", (artistName,))
    artist = c.fetchall()

    # Separating the values into a list and outputting
    artistList = str(artist).split(",")
    print("#" + cleanPrint(artistList[0]) + "." + cleanPrint(artistList[1]))
    print("From" + cleanPrint(artistList[2]) + " with" + cleanPrint(artistList[4]) + " listeners.")
    print("Tags:" + cleanPrint(artistList[3] + " --- Ambiguous:" + cleanPrint(artistList[5])))

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()

# gets all the songs of an artist
def getArtistsLibrary(singerName):
    # Connecting to database
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Returning all song names for an artist
    print("\nAll songs on file for " + singerName + ":\n")
    library = c.execute("SELECT idPk, songNameTxt FROM Songs WHERE artistFpk == ?", (singerName,))
    library = c.fetchall()

    # Outputting the values found that match
    for element in library:
        elementPrint = str(element).split(",")
        print("#" + cleanPrint(elementPrint[0]) + "." + cleanPrint(elementPrint[1]))

    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()


### Metadata Queries ###

# gets the number of artists in the database
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


# gets the number of songs in the database
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


def main():
    # for a song, print the artist, genre, and year
    testsong = "Back To Black"
    print("Song: " + testsong)
    print("Artist: " + getDataOfSong(testsong, ARTIST_FUNC))
    print("Genre: " + getDataOfSong(testsong, GENRE_FUNC))
    print("Year: " + str(getDataOfSong(testsong, YEAR_FUNC)))
    print("Energy: " + str(getDataOfSong(testsong, ENERGY_FUNC)))

    # for the artist of the song, print the country and listeners (cross-table)
    # the result of getDataOfSong(testsong, ARTIST_FUNC) is used as the parameter for getDataOfArtist
    print("Artist Country: " + getDataOfArtist(getDataOfSong(testsong, ARTIST_FUNC), COUNTRY_FUNC))
    print("Artist Listeners: " + str(getDataOfArtist(getDataOfSong(testsong, ARTIST_FUNC), LISTENERS_FUNC)))

if __name__ == "__main__":
    main()
