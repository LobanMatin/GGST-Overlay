import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.support.select import Select

current_character = "Jack-O"

# connect to database for frame data
connection = sqlite3.connect("overlay.db")
cursor = connection.cursor()

# create frame data table
cursor.execute("""
CREATE TABLE IF NOT EXISTS combos (
    combo TEXT PRIMARY KEY,
    position TEXT,
    damage INTEGER,
    character TEXT,
    FOREIGN KEY (character) REFERENCES characters(character_name)
)       
""")

# open webpage using selenium
driver = webdriver.Chrome()
url = "https://www.dustloop.com/w/GGST/" + current_character + "/Combos"
driver.get(url)
driver.maximize_window()
time.sleep(3)

# select optimal combos
for i in range(2, 6):
    driver.find_element("id", "tab-Optimal-" + str(i)).click()

# scrape data from tables
combo_data = []
SPAN = 3

table = driver.find_element("id", "Optimal-2")
rows = table.find_elements("tag name", "tr")[1:]

for i in range(len(rows)):
    row_data = []
    row_elements = rows[i].find_elements("tag name", "td")[:3]
    for x in range(len(row_elements)):
        row_data.append(row_elements[x].text)

    row_data.append(current_character)
    combo_data.append(tuple(row_data))

# add full data to database
for row_data in combo_data:
    cursor.execute('INSERT INTO combos VALUES(?, ?, ?, ?)', row_data)

connection.commit()
connection.close()


