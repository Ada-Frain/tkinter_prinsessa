from tkinter import *
import re


class Kino():
    def __init__(self):
        self.mas = []
        names = []
        for i in range(10):
            self.name = "Кинотеатр" + str(i)
            names.append(self.name)
        self.root = Tk()
        self.root.geometry("300x500")
        self.root.title("Бронирование мест")
        for i in range(10):
            self.ss = i
            self.but = Button(self.root, text=names[i], background="#ccc", foreground="#555", padx="40", pady="8",
                              font="16", width="12", command=self.for_knopki)
            self.but.pack()
        self.board = list(range(1, 10))
        self.root.mainloop()

    def changeBut(self, event):
        event.widget["background"] = "#ffc801"
        abs = re.search("button(\d+)?", str(event.widget))
        self.mas.append(abs[1])

    def for_knopki(self):
        print(self.ss)
        self.root = Tk()
        for i in range(10):
            for j in range(10):
                self.but = Button(self.root, background="#ccc", foreground="#555", padx="20", pady="8", font="16",
                                  width="1")
                asd = str(i) + str(j)
                if asd in self.mas:
                    self.but["bg"] = "#ffc801"
                self.but.configure()
                self.but["text"] = str(j + 1)
                self.but.bind("<Button-1>", self.changeBut)
                self.but.grid(row=i, column=j)
            self.lab = Label(self.root, text="ряд " + str(i))
            self.lab.grid(row=i, column=(j + 1))

if __name__ == '__main__':
    Kino()