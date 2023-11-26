import tkinter as tk
from overlay import Window

from pages.landing.landing import LandingPage




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

        for pg in page_list:
            # create frame and add to dictionary
            page_frame = pg(self, main_frame, root)
            page_frame.configure(bg="white") #are all backgrounds white?
            page_frame.grid(row=0, column=0, sticky="nsew")
            self.page_frames[pg] = page_frame

        # Show landing page on top at the start
        self.page_to_top(LandingPage)
        self.current_page = LandingPage

        # add functionality to adjust overlay translucency
        self.alpha = 1
        root.attributes("-alpha", self.alpha)

        def trans_plus(e):
            if self.alpha <= 0.75:
                self.alpha += 0.25
                root.attributes("-alpha", self.alpha)
            return

        def trans_minus(e):
            if self.alpha >= 0.25:
                self.alpha -= 0.25
                root.attributes("-alpha", self.alpha)
            return

        root.bind("<Control-q>", trans_plus)
        root.bind("<Control-w>", trans_minus)


        # add overlay toggle funtionality
        self.showing = True

        def overlay_toggle(e):
            if self.showing:
                self.showing = False
                page_to_top(OverlayHide)
            else:
                self.showing = True
                page_to_top()

        # add force quit functionality
        def force_quit(e):
            self.root.quit()

        root.bind("<Control-r>", force_quit)

        # helper function to raise desired frame to top
        def page_to_top(page=self.current_page): #MAKE THIS TAKE TEXT ARGUMENT INSTEAD
            if page != OverlayHide:
                self.current_page = page
            page.tkraise()
            return


# main loop to run application
if __name__ == "__main__":
    overlay_app = MainApp()
    Window.launch()



