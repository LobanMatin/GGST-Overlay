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
CREATE TABLE IF NOT EXISTS frame_data (
    input TEXT,
    move_name TEXT,
    damage INTEGER,
    guard TEXT,
    startup INTEGER,
    active INTEGER,
    recovery INTEGER,
    on_block INTEGER,
    on_hit INTEGER,
    character_name TEXT
)       
""")

driver = webdriver.Chrome()
url = "https://www.dustloop.com/w/GGST/" + current_character + "/Frame_Data"
driver.get(url)
driver.maximize_window()
time.sleep(3)

# maximise dropdowns
normal_drop = Select(driver.find_element("name", "DataTables_Table_0_length"))
normal_drop.select_by_index(3)

special_drop = Select(driver.find_element("name", "DataTables_Table_1_length"))
special_drop.select_by_index(3)

over_drop = Select(driver.find_element("name", "DataTables_Table_2_length"))
over_drop.select_by_index(3)

# select data from tables
full_fd = []

for i in range(3):
    # select a table
    table = driver.find_element("id", "DataTables_Table_" + str(i))

    if i == 0:
        span = 9
    else:
        span = 10

    # acquire all the relevant rows
    data = table.find_elements("tag name", "tr")[2:]

    # collect data from each row in the table
    for row in data:
        elements = row.find_elements("tag name", "td")[1:span]
        for y in range(len(elements)):
            elements[y] = elements[y].text

        # normal moves are without name
        if i == 0:
            elements.insert(1, None)

        # add row to full data list
        elements.append(current_character)
        full_fd.append(tuple(elements))

# add full data to database
for row_data in full_fd:
    cursor.execute('INSERT INTO frame_data VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row_data)

connection.commit()
connection.close()




