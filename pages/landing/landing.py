import tkinter as tk
from PIL import ImageTk, Image

logo_img = Image.open("logo.png")

class LandingPage(tk.Frame):
    def __init__(self, controller, parent, root):
        tk.Frame.__init__(self, parent)

        # create frame for buttons
        button_frame = tk.LabelFrame(self, bg="white", bd=0)
        button_frame.place(relx=0, rely=0.5, anchor="n")
        button_dims = (round(controller.width*0.05), round(controller.height*0.005)) #figure out dimensions

        # character select button
        char_button = tk.Button(button_frame, text="Character Select", width=button_dims[0], height=button_dims[1],
                                pady=round(button_dims[1]/2),
                                command=lambda: controller.page_to_top("CharSelect"))
        char_button.grid(row=0, column=0, pady=25) # padding why 25?

        # help/options button
        help_button = tk.Button(button_frame, text="Help/Options", width=button_dims[0], height=button_dims[1],
                                pady=round(button_dims[1]/2),
                                command=lambda: controller.page_to_top("Help"))
        help_button.grid(row=1, column=0, pady=25)

        # exit button
        exit_button = tk.Button(button_frame, text="Exit", width=button_dims[0], height=button_dims[1],
                                pady=round(button_dims[1] / 2),
                                command=root.quit)
        exit_button.grid(row=2, column=0, pady=25)

        # adding title to landing page
        title_canvas = tk.Canvas(self, height=controller.height*0.2, width=controller.width*0.7, bg="white",
                                 highlightthickness=0)
        