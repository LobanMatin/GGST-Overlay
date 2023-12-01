import sqlite3
import tkinter as tk
from pages.data.data_pages import DataPage


class Combos(DataPage):
    def __init__(self, controller, parent, root):
        DataPage.__init__(self, controller, parent, root)

        # define constants for data
        headings = ["Combo", "Position", "Damage"]
        TEXT_PADDING = 0.005
        CELL_DIMS = (controller.width * 0.15, controller.height * 0.03)

        # add headings to page
        for i in range(len(headings)):
            heading_frame = tk.LabelFrame(self.list_frame)
            heading_frame.grid(row=0, column=i)

            heading_canvas = tk.Canvas(heading_frame, width=CELL_DIMS[0], height=CELL_DIMS[1])
            heading_canvas.create_text(controller.width * TEXT_PADDING, controller.width * TEXT_PADDING,
                                       text=headings[i], anchor="nw")
            heading_canvas.pack()

        # retrieve data from database
        connection = sqlite3.connect("C:/Users/Loban Matin/PycharmProjects/GGST_Overlay/scraping/overlay.db")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM combos
            WHERE character = ?
        """, ("Jack-O",))
        combos = cursor.fetchall()

        # print frame data row by row
        for table_row in range(len(combos)):
            combo = combos[table_row][:-1]

            for i in range(len(combo)):
                input_frame = tk.LabelFrame(self.list_frame)
                input_frame.grid(row=table_row + 1, column=i, sticky="nsew")
                input_canvas = tk.Canvas(input_frame, width=CELL_DIMS[0], height=CELL_DIMS[1])

                input_canvas.create_text(controller.width * TEXT_PADDING, controller.width * TEXT_PADDING,
                                         text=combo[i], anchor="nw")
                input_canvas.pack()

