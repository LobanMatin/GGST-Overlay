import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.support.select import Select

# connect to database for frame data
connection = sqlite3.connect("overlay.db")
cursor = connection.cursor()

# create frame data table
cursor.execute("""
CREATE TABLE IF NOT EXISTS frame_data (
    input TEXT
    character_name TEXT
    move_name TEXT
    damage INTEGER
    guard TEXT
    startup INTEGER
    active INTEGER
    recovery INTEGER
    on-block INTEGER
    on-hit INTEGER
)       
""")

driver = webdriver.Chrome()
url = "https://www.dustloop.com/w/GGST/Jack-O/Frame_Data"
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

# select data from tables CHANGE THIS TO SEPERATE FOR EACH TABLE SINCE THEY HAVE DIFFERENT HEADINGS
for i in range(3):
    # select a table
    table = driver.find_element("id", "DataTables_Table_" + str(i))

    # acquire all the relevant rows
    data = table.find_elements("tag name", "tr")[2:]

    # add data from each row to database
    for row in data:
        elements = row.find_elements("tag name", "td")[1:9]
        for y in range(len(elements)):
            elements[y] = elements[y].text

