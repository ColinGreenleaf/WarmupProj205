
# These constants represent the different "functions" which can be passed into some of the 
# getData functions in order to get a specfic field of an artist or song. 

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
    print("All of the songs from " + artist)

# gets one element of data from a song, denoted by the function parameter
def getDataOfSong(songName, function):
    print("The data of " + songName + " with " + str(function))
    if(function == 1):
        return "artist_of_" + songName

# gets one element of data from an artist, denoted by the function parameter
def getDataOfArtist(artistName, function):
    print("The data of " + artistName + " with " + str(function))

# gets all the information of a song
def getSong(songName):
    print("All of the info on " + songName)

# gets all the information of an artist
def getArtist(artistName):
    print("All of the information on" + artistName)

# gets all the songs of an artist
def getArtistsLibrary(singerName):
    print("All of the songs of " + singerName)


### Metadata Queries ###

# gets the number of artists in the database
def getAllArtists():
    print("The number of artists in the database")

# gets the number of songs in the database
def getAllSongs():
    print("The number of artists of a database")

# Checks if all terms used are valid in language and that the name (last word) is enclosed in quotation marks
# Also ensures second to last word is either artist or song
def validQuery(query):
    
    queryLength = len(query)
    if queryLength <= 2:
        print("This query is not long enough. It must be in the format field(s) type \"name\"")
        return False

    # Making sure every word is valid
    validWords = {"country", "tag", "listeners", "song", "artist", "title", "genre", "year", "energy", "dance", "loudness"}
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
    if lastWord[len(lastWord)-1] != '\"':
        print("Please enclose name in quotation marks")
        return False
    
    #Checking second to last word
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

    if nextField == "title":
        title = getDataOfSong(songName, 2)
    elif nextField == "genre":
        getDataOfSong(songName, 3)
    elif nextField == "year":
        getDataOfSong(songName, 4)
    elif nextField == "energy":
        getDataOfSong(songName, 5)
    elif nextField == "dance":
        getDataOfSong(songName, 6)
    elif nextField == "loudness":
        getDataOfSong(songName, 7)
    
    
    elif nextField == "artist":
        if len(fieldsToSearch) == 0:
            getDataOfSong(songName, 1)
        else:
            newQuery = []
            for item in fieldsToSearch:
                newQuery.append(item)
            newQuery.append("artist")
            newQuery.append("\"" + getDataOfSong(songName, 1) + "\"")
            artistSearch(newQuery)
    else:
        print("The field you tried to access does not exist for songs, it must be an artist field")

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
        getDataOfArtist(artistName, 2)
    if nextField == "tag":
        getDataOfArtist(artistName, 3)
    if nextField == "listeners":
        getDataOfArtist(artistName, 4)
    else:
        print("The field you tried to access does not exist for songs, it must be an song field")





def main():
    # Start sequence asking for user input
    print("Welcome to Songify! Please make a query below:")
    print("Remember, names must have dashes instead of spaces")
    query = input("Query Here: ")
    
    # Splitting the query into a list and changing to lowercase
    queryAsList = query.split(" ")    
    queryLength = len(queryAsList)
    for i in range(len(queryAsList)):
        queryAsList[i] = queryAsList[i].lower()

    # Checking if all of the terms in query are valid. If not, take another query
    while not validQuery(queryAsList):
        query = input("Query Here: ")
        queryAsList = query.split(" ")
        for i in range(len(queryAsList)):
            queryAsList[i] = queryAsList[i].lower()

    # Determining what kind of query and running appropriate function
    if queryAsList[queryLength - 2] == "song":
        songSearch(queryAsList)
    elif queryAsList[queryLength - 2] == "artist":
        artistSearch(queryAsList)
    


    

    



main()