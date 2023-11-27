import tkinter as tk
from overlay import Window

from pages.character.character import CharMenu
from pages.landing.landing import LandingPage
from pages.select.select import CharSelect


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
        name_list = ["LandingPage", "CharSelect", "CharMenu"]
        frame_list = [LandingPage, CharSelect, CharMenu]
        for i in range(len(name_list)):
            # create frame and add to dictionary
            page_frame = frame_list[i](self, main_frame, root)
            page_frame.configure(bg="white")  # are all backgrounds white?
            page_frame.grid(row=0, column=0, sticky="nsew")
            self.page_frames[name_list[i]] = page_frame

        # Show landing page on top at the start
        self.page_to_top("LandingPage")
        self.current_page = "LandingPage"

        # helper function to raise desired frame to top

        # add functionality to adjust overlay translucency
        self.alpha = 1
        root.attributes("-alpha", self.alpha)
        root.bind("<Control-q>", self.trans_plus)
        root.bind("<Control-w>", self.trans_minus)

        # add overlay toggle functionality
        self.showing = True

        # quit functionality
        root.bind("<Control-r>", self.force_quit)

    def trans_plus(self, e):
        if self.alpha <= 0.75:
            self.alpha += 0.25
            self.root.attributes("-alpha", self.alpha)
        return

    def trans_minus(self, e):
        if self.alpha >= 0.25:
            self.alpha -= 0.25
            self.root.attributes("-alpha", self.alpha)
        return

    def overlay_toggle(self, e):
        if self.showing:
            self.showing = False
            self.page_to_top(LandingPage)  # CHANGE TO OVERLAY HIDE LATER
        else:
            self.showing = True
            self.page_to_top()

    # add force quit functionality
    def force_quit(self, e):
        self.root.quit()

    def page_to_top(self, page=""):  # MAKE THIS TAKE TEXT ARGUMENT INSTEAD
        if page == "":  # CHANGE TO OVERLAY HIDE LATER
            page = self.current_page
        self.page_frames[page].tkraise()
        self.current_page = page
        return


# main loop to run application
if __name__ == "__main__":
    overlay_app = MainApp()
    Window.launch()
