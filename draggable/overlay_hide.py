import tkinter as tk
from PIL import ImageTk, Image
from draggable.drag_manager import DraggableWidgets

overlay_logo = Image.open("draggable/OverlayLogo.png")


class OverlayHide(tk.Frame):
    def __init__(self, controller, parent, root, ):
        tk.Frame.__init__(self, parent)

        # Define global variables
        global overlay_logo

        # Set overlay background to be transparent
        self.configure(bg="white")

        # Create Button
        button = tk.Button(self)
        dw = DraggableWidgets()
        dw.add_widget(button, controller.width, controller.height)
        overlay_logo = overlay_logo.resize((150, 150))
        overlay_logo = ImageTk.PhotoImage(overlay_logo, master= button)
        button.configure(width=250, height=250, bg="white", image=overlay_logo, bd=0, activebackground="white")

        button.place(relx=0.5, rely=0.5, anchor="center")
