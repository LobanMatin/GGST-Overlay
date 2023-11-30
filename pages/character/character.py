import tkinter as tk
from PIL import ImageTk, Image

jacko_menu = Image.open("pages/character/JackO_Menu.png")


class CharMenu(tk.Frame):
    def __init__(self, controller, parent, root):
        tk.Frame.__init__(self, parent)

        # images need to be global variables
        global jacko_menu

        # create frame for buttons
        button_frame = tk.LabelFrame(self, bg="white", bd=0)
        button_frame.place(relx=0.5, rely=0.5, anchor="n")

        button_dims = (round(controller.width * 0.05), round(controller.height * 0.005))

        # frame data button
        fd_button = tk.Button(button_frame, text="Frame Data", width=button_dims[0], height=button_dims[1],
                              pady=round(button_dims[1] / 2), command=lambda: controller.page_to_top("FrameData"))
        fd_button.grid(row=0, column=0, pady=25)

        # data button
        com_button = tk.Button(button_frame, text="Combos", width=button_dims[0], height=button_dims[1],
                               pady=round(button_dims[1] / 2), command=lambda: controller.page_to_top("Combos"))
        com_button.grid(row=1, column=0, pady=25)

        # back button
        back_button = tk.Button(button_frame, text="Back", width=button_dims[0], height=button_dims[1],
                                pady=round(button_dims[1] / 2), command=lambda: controller.page_to_top("CharSelect"))
        back_button.grid(row=2, column=0, pady=25)

        # creating canvas for heading
        title_canvas = tk.Canvas(self, height=controller.height * 0.4, width=controller.width * 0.7, bg="white",
                                 highlightthickness=0)

        jacko_menu = jacko_menu.resize((round(controller.width * 0.7), round(controller.height * 0.4)), Image.LANCZOS)
        jacko_menu = ImageTk.PhotoImage(jacko_menu, master=title_canvas)
        title_canvas.create_image(0, 0, image=jacko_menu, anchor="nw")

        title_canvas.place(relx=0.5, rely=0.1, anchor='n') # ADD API INFO AND CHAR IMG TO CANVAS

