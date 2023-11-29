import sqlite3

# setup database for overlay
connection = sqlite3.connect("overlay.db")
cursor = connection.cursor()

# create characters table
cursor.execute("""
CREATE TABLE IF NOT EXISTS characters (
    character_name TEXT PRIMARY KEY
)       
""")

# add character names to database INSERT MORE CHARACTERS
cursor.execute("""
INSERT INTO characters VALUES
('Jack-O')
""")

connection.commit()
connection.close()