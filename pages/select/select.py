import tkinter as tk

jacko_img = tk.PhotoImage(file="pages/select/jacko_face.png")


class CharSelect(tk.Frame):
    def __init__(self, controller, parent, root):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # images need to be global variables
        global jacko_img

        # create frame for character buttons
        button_frame = tk.LabelFrame(self, bg="white", bd=0)
        button_frame.pack(side="top", fill="both", expand=True)

        button_dims = (round(controller.width * 0.02), round(controller.height * 0.003))

        # back button to return to landing page
        back_button = tk.Button(button_frame, text="Back", width=button_dims[0], height=button_dims[1],
                                pady=round(button_dims[1] / 2), command=lambda: controller.page_to_top("LandingPage"))
        back_button.place(relx=0.05, rely=0.95, anchor="sw")

        # character buttons
        jacko_button = tk.Button(button_frame, image=jacko_img, width=button_dims[0]*5, height=button_dims[0]*5,
                                 command=lambda: self.change_char("Jack-O"))
        jacko_button.place(relx=0.5, rely=0.5, anchor="center")

    def change_char(self, char):
        self.controller.select_character = char
        self.controller.page_to_top("CharMenu")
        return
