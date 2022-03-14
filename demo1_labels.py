import tkinter


class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.main_window, text="John")

        self.label2 = tkinter.Label(self.main_window, text="Jill")

        self.label3 = tkinter.Label(self.main_window, text="James")

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label4 = tkinter.Label(self.main_window, text="Jack")

        self.label5 = tkinter.Label(self.main_window, text="Jim")

        self.label6 = tkinter.Label(self.main_window, text="Jerry")

        self.label1.pack(side="left")
        self.label2.pack(side="left")
        self.label3.pack(side="left")

        self.mybutton = tkinter.Button(
            self.main_window, text="Click me", command=self.do_something
        )
        self.quitbutton = tkinter.Button(
            self.main_window, test="Quit", command=self.main_window.destroy
        )

        self.mybutton.pack(side="top")
        self.quitbutton.pack(side="top")

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Response", "Thanks")


my_gui = MyGUI()

print("Moving On...")
