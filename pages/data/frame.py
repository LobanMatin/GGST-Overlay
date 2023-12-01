import sqlite3
import tkinter as tk
from tkinter import ttk

from converter.converter import move_to_img
from pages.data.data_pages import DataPage


class FrameData(DataPage):
    def __init__(self, controller, parent, root):
        DataPage.__init__(self, controller, parent, root)

        # define constants for data
        headings = ["Input", "Name", "Damage", "Guard", "Start-Up", "Active", "Recovery", "On-Block", "On-Hit"]
        TEXT_PADDING = 0.005
        CELL_DIMS = (controller.width * 0.15, controller.height * 0.03)

        # add headings to page
        for i in range(len(headings)):
            heading_frame = tk.LabelFrame(self.list_frame, text=headings[i], height=20, width=200)
            heading_frame.grid(row=0, column=i)

        # retrieve data from database
        connection = sqlite3.connect("C:/Users/Loban Matin/PycharmProjects/GGST_Overlay/scraping/overlay.db")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM frame_data
            WHERE character = ?
        """, ("Jack-O",))
        frame_data = cursor.fetchall()

        # print frame data row by row
        for table_row in range(-1, len(frame_data)):
            for i in range(len(headings)):
                input_canvas = tk.Canvas(self.list_frame)
                if table_row == -1:
                    input_canvas.create_text(controller.width * TEXT_PADDING, controller.width * TEXT_PADDING,
                                             text=headings[i], anchor="nw")
                else:
                    move = frame_data[table_row][:-1]

                    if not (move[i]):
                        cell_text = "N/A"
                    else:
                        cell_text = move[i]

                    if i == 0:
                        move_to_img(cell_text, input_canvas)
                    else:
                        input_canvas.create_text(controller.width * TEXT_PADDING, controller.width * TEXT_PADDING,
                                                 text=cell_text, anchor="nw")

                if i == 0:
                    new_width = 300
                else:
                    new_width = 10

                input_canvas.grid(row=table_row + 1, column=i, sticky="nsew")
                input_canvas.configure(highlightthickness=1, width=0, height=30, highlightbackground="black")
