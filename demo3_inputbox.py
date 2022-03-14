import tkinter
import tkinter.messagebox


class KiloGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.geometry("500X200")
        self.main_window.title("Label Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt = tkinter.Label(self.main_window, text="Kilometers?")
        self.kilos = tkinter.Entry(self.top_frame, width=10)

        self.prompt.pack(side="left")
        self.kilos.pack(side="left")

        self.calcbutton = tkinter.Button(
            self.main_window, text="Convert", command=self.convert
        )
        self.quitbutton = tkinter.Button(
            self.main_window, test="Quit", command=self.main_window.destroy
        )

        self.mybutton.pack(side="left")
        self.quitbutton.pack(side="left")

        tkinter.mainloop()

    def convert(self):

        kilo = float(self.kilos.get())

        miles = round(kilo * 0.6214, 2)

        tkinter.messagebox.showinfo(
            "Result", str(kilo) + " kilometers is equal to " + str(miles) + "mile."
        )


kiloconv = KiloGUI()


print("Moving On...")
