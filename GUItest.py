import tkinter
from tkinter.ttk import Frame


class score:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.geometry("300x150")
        self.main_window.title("Test Average")

        self.topf = tkinter.Frame(self.main_window)
        self.midf = tkinter.Frame(self.main_window)
        self.bottf = tkinter.Frame(self.main_window)
        self.avgf = tkinter.Frame(self.main_window)

        self.t1 = tkinter.Label(self.topf, text="Enter the Score for Test 1?")
        self.s1 = tkinter.Entry(self.topf, width=10)
        self.t1.pack(side="left")
        self.s1.pack(side="left")

        self.t2 = tkinter.Label(self.midf, text="Enter the Score for Test 2?")
        self.s2 = tkinter.Entry(self.midf, width=10)
        self.t2.pack(side="left")
        self.s2.pack(side="left")

        self.t3 = tkinter.Label(self.bottf, text="Enter the Score for Test 3?")
        self.s3 = tkinter.Entry(self.bottf, width=10)
        self.t3.pack(side="left")
        self.s3.pack(side="left")

        self.avg = tkinter.Label(self.avgf, text="Average:")
        self.avgvar = tkinter.StringVar()
        self.avglabel = tkinter.Label(self.avgf, textvariable=self.avgvar)
        self.avg.pack(side="left")
        self.avglabel.pack(side="left")

        self.calc = tkinter.Button(
            self.main_window, text="Calculate", command=self.calc
        )
        self.calc.pack(side="bottom")

        self.quit = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )
        self.quit.pack(side="bottom")

        self.topf.pack(side="top")
        self.midf.pack(side="top")
        self.bottf.pack(side="top")
        self.avgf.pack(side="top")

        tkinter.mainloop()

    def calc(self):

        average = (
            float(self.s1.get()) + float(self.s2.get()) + float(self.s3.get())
        ) / 3

        self.avgvar.set(average)

        print(average)


test = score()
