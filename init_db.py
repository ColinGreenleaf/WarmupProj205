import sqlite3

# Function to open the csvs and read in the values into the databases
def dbMaker(artistFile, songFile):
    # Creating the database and connecting to it
    print("Connecting to the database...")
    conn = sqlite3.connect('topRecords.db')
    c = conn.cursor()

    # Creating the tables
    print("Creating the table Artists...")
    c.execute('''CREATE TABLE Artists(
        idPk INTEGER PRIMARY KEY AUTOINCREMENT, artistFpk text, 
        countryTxt text, tagsTxt text, listenersInt int, ambiguousTxt text)''')
    print("Creating the table Songs...")
    c.execute('''CREATE TABLE Songs(
        idPk INTEGER PRIMARY KEY AUTOINCREMENT, artistFpk text, 
        songNameTxt text, genreTxt text, yearInt int, energyInt int, danceabilityInt int, loudnessInt int)''')
    
    # Finishing the table and database creation
    print("Committing the table creations...")
    conn.commit()
    print("Successfully created the tables!")

    # Filling the Artists table from the artistSet csv
    reader = open(artistFile, "r")
    artistPmk = 1
    for element in open(artistFile):
        # Placing the current line into a temporary variable
        line = reader.readline()
        lineList = line.split(",")

        # Filling lists to add values from if it is not the first line of the csv
        if lineList[1] == "artist_mb":
            print("Passing the csv labels...")
        else:
            artistToInsert =[(artistPmk, lineList[1], lineList[3], lineList[5], lineList[7], lineList[9])]

            # Big try/except statement to catch issues with duplicates and return success messages
            try:
                # Committing the insert values
                c.executemany("INSERT INTO Artists VALUES (?, ?, ?, ?, ?, ?)", artistToInsert)
                conn.commit()
            except sqlite3.IntegrityError:
                print("Error. Tried to add duplicate record!")
            else:
                artistPmk += 1
    print("Successfully added all artist records!")
    reader.close()

    # Fillings the Songs table from the songSet csv
    reader = open(songFile, "r")
    songPmk = 1
    for element in open(songFile):
        # Placing the current line into a temporary variable
        line = reader.readline()
        lineList = line.split(",")

        # Filling lists to add values from if it is not the first line of the csv
        if lineList[1] == "Title":
            print("Passing the csv labels...")
        else:
            songToInsert =[(songPmk, lineList[2], lineList[1], lineList[3], lineList[4], lineList[6], lineList[7], lineList[8])]

            # Big try/excpet statement to catch issues with duplciates and return success messages
            try:
                # Commiting the insert values
                c.executemany("INSERT INTO Songs VALUES (?, ?, ?, ?, ?, ?, ?, ?)", songToInsert)
                conn.commit()
            except sqlite3.IntegrityError:
                print("Error. Tried to add duplicate record!")
            else:
                songPmk += 1
    print("Successfully added all song records!")
    reader.close()
        
    # Closing connection
    if c is not None:
        c.close()
    if conn is not None:
        conn.close()