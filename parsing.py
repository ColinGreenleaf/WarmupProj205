import shlex

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

# Checks if all terms used are valid in language and that the name (last word) is enclosed in quotation marks
# Also ensures second to last word is either artist or song
def validQuery(query):
    queryLength = len(query)
    if queryLength <= 2:
        print("This query is not long enough. It must be in the format field(s) type \"name\"")
        return False

    # Making sure every word is valid
    validWords = {"country", "tag", "listeners", "song", "artist", "title", "genre", "year", "energy", "dance",
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
    elif nextField == "tag":
        print("the tags of the artist " + artistName + " are: " + db.getDataOfArtist(artistName, TAGS_FUNC))
    elif nextField == "listeners":
        print("the number of listeners of the artist " + artistName + " is: " + str(db.getDataOfArtist(artistName, LISTENERS_FUNC)))
    else:
        print("The field " + nextField + " is a song field. It does not exist for artists.")





def makeQuery(query):
    # Splitting the query into a list
    queryAsList = shlex.split(query, posix=False)
    queryLength = len(queryAsList)

    if query == "metadata songs":
        print(db.getAllSongs())
    elif query == "metadata artists":
        print(db.getAllArtists())
    else:
        # Checking if all of the terms in query are valid. If not, take another query
        while not validQuery(queryAsList):
            if query == "metadata songs":
                print(db.getAllSongs())
            elif query == "metadata artists":
                print(db.getAllArtists())
            query = input("Query Here: ")
            queryAsList = shlex.split(query, posix=False)

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
        makeQuery(queryToMake)

main()
# def testing():
#     makeQuery("loudness song \"The Real Slim Shady\"")
#
# testing()