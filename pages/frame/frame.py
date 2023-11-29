import sqlite3
import tkinter as tk
from tkinter import ttk


class FrameData(tk.Frame):
    def __init__(self, controller, parent, root):
        tk.Frame.__init__(self, parent)

        # create a canvas to contain data
        data_canvas = tk.Canvas(self)
        data_canvas.configure(bg="white", bd=0, highlightthickness=0)
        data_canvas.grid(row=0, column=1, sticky="nsew")

        # create a vertical scrollbar
        sv_frame = tk.LabelFrame(self)
        scroll_vert = ttk.Scrollbar(sv_frame, orient="vertical", command=data_canvas.yview)
        scroll_vert.pack(fill="y", side="right", expand=True)
        sv_frame.grid(row=0, column=2, sticky="nsew")

        data_canvas.configure(yscrollcommand=scroll_vert.set)
        data_canvas.bind("<Configure>", lambda e: data_canvas.configure(scrollregion=data_canvas.bbox("all")))

        # create a horizontal scrollbar
        hv_frame = tk.LabelFrame(self)
        hv_frame.grid(row=1, column=1, sticky="nsew")
        scroll_hor = ttk.Scrollbar(hv_frame, orient="horizontal", command=data_canvas.xview)
        scroll_hor.pack(fill="x", expand=True, side="bottom")


        data_canvas.configure(xscrollcommand=scroll_hor.set)
        data_canvas.bind("<Configure>", lambda e: data_canvas.configure(scrollregion=data_canvas.bbox("all")))

        # create frame for data within scroll region
        list_frame = tk.LabelFrame(data_canvas)
        data_canvas.create_window((0, 0), window=list_frame, anchor="nw")

        # back button
        button_frame = tk.LabelFrame(self, bd=0, bg="white")
        button_frame.grid(row=0, column=0, sticky="n")
        button_dims = (round(controller.width * 0.02), round(controller.height * 0.003))
        back_button = tk.Button(button_frame, text="Back", width=button_dims[0], height=button_dims[1], bd=0,
                                command=lambda: controller.page_to_top("CharMenu"))
        back_button.pack()

        # configure grid layout
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # define constants for data
        headings = ["Input", "Name", "Damage", "Guard", "Start-Up", "Active", "Recovery", "On-Block", "On-Hit"]
        TEXT_PADDING = 0.005
        CELL_DIMS = (controller.width * 0.15, controller.height * 0.03)

        # add headings to page
        for i in range(len(headings)):
            heading_frame = tk.LabelFrame(list_frame)
            heading_frame.grid(row=0, column=i)

            heading_canvas = tk.Canvas(heading_frame, width=CELL_DIMS[0], height=CELL_DIMS[1])
            heading_canvas.create_text(controller.width * TEXT_PADDING, controller.width * TEXT_PADDING,
                                       text=headings[i], anchor="nw")
            heading_canvas.pack()

        # retrieve data from database
        connection = sqlite3.connect("C:/Users/Loban Matin/PycharmProjects/GGST_Overlay/scraping/overlay.db")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM frame_data
            WHERE character = ?
        """, ("Jack-O",))
        frame_data = cursor.fetchall()

        # print frame data row by row
        for table_row in range(len(frame_data)):
            move = frame_data[table_row][:-1]

            for i in range(len(move)):
                input_frame = tk.LabelFrame(list_frame)
                input_frame.grid(row=table_row + 1, column=i, sticky="nsew")
                input_canvas = tk.Canvas(input_frame, width=CELL_DIMS[0], height=CELL_DIMS[1])

                if move[i] == None:
                    cell_text = "N/A"
                else:
                    cell_text = move[i]

                # if i == 0:
                #     move_to_img(cell_text, input_canvas)
                # else:
                #     input_canvas.create_text(controller.width*TEXT_PADDING, controller.width*TEXT_PADDING,
                #                              text=cell_text, anchor="nw")

                input_canvas.create_text(controller.width * TEXT_PADDING, controller.width * TEXT_PADDING,
                                         text=cell_text, anchor="nw")

                input_canvas.pack()






