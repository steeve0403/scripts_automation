import sqlite3

connection = sqlite3.connect('albums2.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE artist (
    artist_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR
    );
""")

connection.commit()
connection.close()