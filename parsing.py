import shlex
import init_db as init_db
import os.path

import db as db
# These constants represent the different "functions" which can be passed into some of the 
# getData functions in order to get a specific field of an artist or song.

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

# Constants for csv files
ARTIST_CSV = "artistSet.csv"
SONG_CSV = "songSet.csv"


# Checks if all terms used are valid in language and that the name (last word) is enclosed in quotation marks
# Also ensures second to last word is either artist or song
def validQuery(query):
    queryLength = len(query)
    if queryLength <= 2:
        print("This query is not long enough. It must be in the format field(s) type \"name\"")
        return False

    # Making sure every word is valid
    validWords = {"country", "tags", "listeners", "song", "artist", "title", "genre", "year", "energy", "dance",
                  "loudness"}
    for word in query:
        if word[0] != '\"':
            if word not in validWords:
                print("Invalid word used in query")
                return False
    # Checking last word
    lastWord = query[queryLength - 1]
    if lastWord[0] != '\"':
        print("Please enclose name in quotation marks")
        return False
    if lastWord[len(lastWord) - 1] != '\"':
        print("Please enclose name in quotation marks")
        return False

    # Checking second to last word
    secondToLast = query[queryLength - 2]
    if secondToLast != "song" and secondToLast != "artist":
        print("The term before name should be either song or artist according to search. Please make another query")
        return False

    return True


def songSearch(query):
    queryLength = len(query)

    # Cleaning up songName
    songName = query[queryLength - 1]
    songName = songName.replace("\"", "")
    songName = songName.replace("-", " ")

    # Adding the rest of the fields to query

    fieldsToSearch = []
    for i in range(queryLength - 2):
        fieldsToSearch.append(query[i])

    fieldsLength = len(fieldsToSearch)

    # Calling all of the "easy" functions for song
    nextField = fieldsToSearch.pop()

    try:
        if nextField == "title":
            print("The title of the song " + songName + " is: " + db.getDataOfSong(songName, TITLE_FUNC))
        elif nextField == "genre":
            print("The genre of the song " + songName + " is: " + db.getDataOfSong(songName, GENRE_FUNC))
        elif nextField == "year":
            print("The year of the song " + songName + " is: " + str(db.getDataOfSong(songName, YEAR_FUNC)))
        elif nextField == "energy":
            print("The energy of the song " + songName + " is: " + str(db.getDataOfSong(songName, ENERGY_FUNC)))
        elif nextField == "dance":
            print("The danceability of the song " + songName + " is: " + str(db.getDataOfSong(songName, DANCE_FUNC)))
        elif nextField == "loudness":
            print("The loudness of the song " + songName + " is: " + str(db.getDataOfSong(songName, LOUD_FUNC)))


        elif nextField == "artist":
            if len(fieldsToSearch) == 0:
                print("the name of the artist of \"" + songName + "\" is: " + db.getDataOfSong(songName, ARTIST_FUNC))
            else:
                newQuery = []
                for item in fieldsToSearch:
                    newQuery.append(item)
                newQuery.append("artist")
                newQuery.append("\"" + db.getDataOfSong(songName, ARTIST_FUNC) + "\"")
                print("the name of the artist of \"" + songName + "\" is: " + db.getDataOfSong(songName, ARTIST_FUNC))
                artistSearch(newQuery)
        else:
            print("The field " + nextField + " is an artist field. It does not exist for songs.")

    except:
        print("Song not found")

def artistSearch(query):
    queryLength = len(query)


    # Getting artist name and cleaning up
    artistName = query[queryLength - 1]
    artistName = artistName.replace("\"", "")
    artistName = artistName.replace("-", " ")

    fieldsToSearch = []
    for i in range(queryLength - 2):
        fieldsToSearch.append(query[i])

    fieldsLength = len(fieldsToSearch)

    # Calling all of the "easy" functions for song
    nextField = fieldsToSearch.pop()

    if nextField == "country":
        print("the country of the artist " + artistName + " is: " + db.getDataOfArtist(artistName, COUNTRY_FUNC))
    elif nextField == "tags":
        print("the tags of the artist " + artistName + " are: " + db.getDataOfArtist(artistName, TAGS_FUNC))
    elif nextField == "listeners":
        print("the number of listeners of the artist " + artistName + " is: " + str(db.getDataOfArtist(artistName, LISTENERS_FUNC)))
    else:
        print("The field " + nextField + " is a song field. It does not exist for artists.")





def makeQuery(query):
    # Splitting the query into a list
    while True:
        try:
            queryAsList = shlex.split(query, posix=False)
            queryLength = len(queryAsList)
            break
        except:
            print("Fully enclose artist/song names in quotation marks")
            query = input("Query Here: ")


    if query == "metadata songs":
        print(db.getAllSongs())
    elif query == "metadata artists":
        print(db.getAllArtists())
    elif query == "help":
        print("--------------------HELP--------------------")
        print("How to use Songify:")
        print("if the database has not been loaded, type \"load data\" to load the database")
        print("the data that you can get from a song is: title, genre, year, energy, dance, loudness, artist")
        print("the data that you can get from an artist is: country, tags, listeners")
        print("to make a query, type the data you want to get, followed by the word song or artist, followed by the name of the song or artist in quotation marks")
        print("the names of songs and artists are Case Sensitive.")
        print("Some example queries:")
        print("to get the artist of the song \"Photograph\", you would type: artist song \"Photograph\"")
        print("to get the country of the artist \"Ed Sheeran\", you would type: country artist \"Ed Sheeran\"")
        print("you can also get info about the artist of a song without having to type the name of the artist. ")
        print("For example, to get the country of the artist of the song \"Photograph\", you would type: country artist song \"Photograph\"")
        print("in that example, the program would first get the artist of the song \"Photograph\", then get the country of that artist")
        print("to get the number of items in a given database, type either metadata songs OR metadata artists")
        print("to get this help menu again, type help")
        print("to exit the program, type exit")
        print("--------------------------------------------")

    elif query == "load data":
        # check if database has already been loaded using os.path.exists
        if os.path.exists("topRecords.db"):
            print("Database already loaded")
        else:
            init_db.dbMaker(ARTIST_CSV, SONG_CSV)

    else:
        # Checking if all of the terms in query are valid. If not, take another query
        while not validQuery(queryAsList):
            if query == "metadata songs":
                print(db.getAllSongs())
            elif query == "metadata artists":
                print(db.getAllArtists())
            query = input("Query Here: ")
            while True:
                try:
                    queryAsList = shlex.split(query, posix=False)
                    queryLength = len(queryAsList)
                    break
                except:
                    print("Fully enclose artist/song names in quotation marks")
                    query = input("Query Here: ")

        # Determining what kind of query and running appropriate function
        if queryAsList[queryLength - 2] == "song":
            songSearch(queryAsList)
        elif queryAsList[queryLength - 2] == "artist":
            artistSearch(queryAsList)
    
def main():
    # Start sequence asking for user input
    print("Welcome to Songify! Please make a query below:")
    complete = False
    while not complete:
        queryToMake = input("Query Here, or type \"exit\" to exit: ")
        if(queryToMake == "exit"):
            complete = True
            break
        try:
            makeQuery(queryToMake)
        except:
            print("Artist or song not found. Please try again.")


if __name__ == "__main__":
    main()
