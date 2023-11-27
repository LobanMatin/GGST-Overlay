import tkinter as tk
from bs4 import BeautifulSoup
import requests


class FrameData(tk.Frame):
    def __init__(self, controller, parent, root):
        tk.Frame.__init__(self, parent)

        # scrape frame data depending on character
        page = requests.get("https://www.dustloop.com/w/GGST/" + controller.select_character + "/Frame_Data")
        soup = BeautifulSoup(page.text, "html.parser")
        
