import sqlite3

connexion = sqlite3.connect("albums.db")
cursor = connexion.cursor()

# cursor.execute("SELECT * FROM artist")
# cursor.execute("SELECT name FROM artist")
# artists = cursor.fetchall()
# for artist in artists:
#     print(artist[1])

# for artist in cursor.execute("SELECT * FROM artist"):
#     print(artist)

cursor.execute(
    "SELECT title FROM album a JOIN artist ar ON a.artist_id = ar.artist_id AND ar.name = 'Céline Dion'"
).fetchall()

cursor.close()
