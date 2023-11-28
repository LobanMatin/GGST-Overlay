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
        scroll_hor = ttk.Scrollbar(sv_frame, orient="horizontal", command=data_canvas.xview)
        scroll_hor.pack(fill="x", expand=True, side="bottom")
        hv_frame.grid(row=1, column=1, sticky="nsew")

        data_canvas.configure(xscrollcommand=scroll_hor.set)
        data_canvas.bind("<Configure>", lambda e: data_canvas.configure(scrollregion=data_canvas.bbox("all")))

        # create frame for data within scroll region
        list_frame = tk.LabelFrame(data_canvas)
        data_canvas.create_window((0, 0), window=list_frame, anchor="nw")

        # back button
        button_frame = tk.LabelFrame(self, bd=0, bg="white")
        button_frame.grid(row=0, column=0, sticky="n")
        button_dims = (round(controller.width*0.02), round(controller.height*0.003))
        back_button = tk.Button(button_frame, text="Back", width=button_dims[0], height=button_dims[1], bd=0,
                                command=lambda: controller.page_to_top("CharMenu"))
        back_button.pack()

        # configure grid layout
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # define constants for data
        headings = ["Input", "Name", "Damage", "Guard", "Start-Up", "Active", "Recovery", "On-Block", "On-Hit"]
        TEXT_PADDING = 0.005
        CELL_DIMS = (controller.width*0.15, controller.height*0.03)
        move_row = 0

        # retrieve data from database


        for i in range(len(headings)):
            heading_frame = tk.LabelFrame(list_frame)
            heading_frame.grid(row=move_row, column=i)

            heading_canvas = tk.Canvas(heading_frame, width=CELL_DIMS[0], height=CELL_DIMS[1])
            heading_canvas.create_text(controller.width*TEXT_PADDING, controller.width*TEXT_PADDING, text=headings[i],
                                       anchor="nw")
            heading_canvas.pack()



        is_not_heading = False
