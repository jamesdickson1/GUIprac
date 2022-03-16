import tkinter
import tkinter.messagebox


class KiloGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Label Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb_var1 = tkinter.Checkbutton(
            self.top_frame, text="Option 1", variable=self.cb_var1
        )
        self.cb_var2 = tkinter.Checkbutton(
            self.top_frame, text="Option 2", variable=self.cb_var2
        )
        self.cb_var3 = tkinter.Checkbutton(
            self.top_frame, text="Option 3", variable=self.cb_var3
        )

        self.cb_var1.pack()
        self.cb_var2.pack()
        self.cb_var3.pack()

        self.calcbutton = tkinter.Button(self.main_window, text="Ok", command=self.do)
        self.quitbutton = tkinter.Button(
            self.main_window, test="Quit", command=self.main_window.destroy
        )

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")
        self.mybutton.pack(side="left")
        self.quitbutton.pack(side="left")

        tkinter.mainloop()

    def do(self):

        self.message = "Selected:"
        tkinter.messagebox.showinfo("response", self.message)


kiloconv = KiloGUI()


print("Moving On...")
