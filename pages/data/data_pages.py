import tkinter as tk
from tkinter import ttk


class DataPage(tk.Frame):
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
        self.list_frame = tk.LabelFrame(data_canvas)
        data_canvas.create_window((0, 0), window=self.list_frame, anchor="nw")

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
