import tkinter as tk
from overlay import Window

class MainApp(Window):
    def __init__(self):

        Window.__init__(self)

        # set root of overlay
        root = self.root
        root.title("GGST Game Overlay")

        # configure root of overlay
        root.wm_attributes("-topmost", True)
        root.overrideredirect(True)
        root.state("zoomed")

        # create frame to hold pages of overlay
        main_frame = tk.Frame(root)
        main_frame.pack(side="top", fill="both", expand=True)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # acquire window dimensions
        root.update()
        self.width = root.winfo_width()
        self.height = root.winfo_height()

        # dictionary to hold pages and their respective frames to switch between pages
        self.page_frames = {}
        page_list = []

        for page in page_list:

            page_frame = page()

            self.page_frames[page] = page_frame


