from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.dustloop.com/w/GGST/Jack-O/Frame_Data")
soup = BeautifulSoup(page.text, "lxml")

tables = soup.find("table", id="DataTables_Table_0")
print(tables)

