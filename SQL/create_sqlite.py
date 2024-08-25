import sqlite3

connection = sqlite3.connect('albums2.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE artist (
    artist_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR
    );
""")

cursor.execute("""
    CREATE TABLE album (
        album_id INTEGER NOT NULL PRIMARY KEY,
        artist_id INTEGER REFERENCES artist,
        title VARCHAR,
        release_date INTEGER
    );
""")

cursor.execute(f'INSERT INTO artist (name) VALUES ("Mickael Jackson");')
mj_id = cursor.lastrowid
cursor.execute(f'INSERT INTO artist (name) VALUES ("Céline Dion");')
cd_id = cursor.lastrowid

cursor.execute(f'INSERT INTO album (artist_id, title, release_date) VALUES ({str(mj_id)}, "Thriller", 1983);')
cursor.execute(f'INSERT INTO album (artist_id, title, release_date) VALUES ({str(cd_id)}, "Falling into you", 1996);')
cursor.execute(f'INSERT INTO album (artist_id, title, release_date) VALUES ({str(cd_id)}, "Let\'s talk about love", 1997);')


connection.commit()
connection.close()