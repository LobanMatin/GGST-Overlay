#https://www.youtube.com/watch?v=6lIt0TI2cG0

# class to create tkinter widgets that are draggable
class DraggableWidgets():
    def add_widget(self, widget, win_width, win_height):
        self.widget = widget
        self.win_width = win_width
        self.win_height = win_height
        self.root = widget.winfo_toplevel()
        self.widget.bind("<B1-Motion>", self.dragging)
        self.widget.bind("<ButtonRelease>", self.stop_drag)
        self.widget.configure(cursor="hand1")

    def dragging(self, event):
        self.widget.place(x=self.root.winfo_pointerx()-(self.win_width/2),
                          y=self.root.winfo_pointery()-(self.win_height/2))

    def stop_drag(self, event):
        self.widget.place(x=self.root.winfo_pointerx() - (self.win_width / 2),
                          y=self.root.winfo_pointery() - (self.win_height / 2))