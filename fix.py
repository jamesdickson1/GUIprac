import tkinter


class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.main_window, text="John")
        self.label1.pack(side="top")

        tkinter.mainloop()


my_gui = MyGUI()

print("show")
