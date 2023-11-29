import sqlite3

connection = sqlite3.connect("C:/Users/Loban Matin/PycharmProjects/GGST_Overlay/scraping/overlay.db")
cursor = connection.cursor()
cursor.execute("""
    SELECT * FROM frame_data
    WHERE character = ?
""", ("Jack-O",))

frame_data = cursor.fetchall()
print(len(frame_data))
