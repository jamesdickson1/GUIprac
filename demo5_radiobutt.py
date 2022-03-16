import tkinter
import tkinter.messagebox


class KiloGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window.title("Label Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        # set the intvar to 1
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="Option 1", variable=self.radio_var, value=10
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="Option 2", variable=self.radio_var, value=20
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="Option 3", variable=self.radio_var, value=30
        )

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.top_frame.pack(side="top")

        self.bottom_frame.pack(side="top")

        self.okbutton = tkinter.Button(
            self.bottom_frame, text="Ok", command=self.show_choice
        )
        self.resetbutton = tkinter.Button(
            self.bottom_frame, test="Reset", command=self.rb1.select
        )

        self.okbutton.pack(side="left")
        self.resetbutton.pack(side="left")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", "You have selected option" + str(self.radio_var.get())
        )


radio = KiloGUI()


print("Moving On...")
