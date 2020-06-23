from tkinter import *
from random import choices
from PIL import ImageTk,Image


class Game():
    def __init__(self):
        self.level = 1
        self.hearts = 5
        self.root = Tk()
        self.root.geometry(f'600x550+{self.root.winfo_screenwidth()//2 - 300}+{self.root.winfo_screenheight()//2 - 300}')
        self.root.title("АльцГеймер")

        self.root["bg"] = "medium sea green"
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.frame1 = Frame(self.root, bg='medium sea green', bd=5)
        self.frame1.grid(column=0, row=0)

        self.playBtn = Button(self.frame1, text="Play!", width=8, height=1, bg='green yellow', fg='#0a4500', font=("comic sans ms", 32), state=DISABLED, command=self.play)
        self.playBtn.grid(column=0, row=0, columnspan=3)

        self.var = IntVar()
        self.diffRbtn1 = Radiobutton(self.frame1, text='Easy', bg='medium sea green', fg='#0a4500', font=("comic sans ms", 13), variable=self.var, value=4, command=self.diffSelect)
        self.diffRbtn1.grid(column=0, row=1)
        self.diffRbtn2 = Radiobutton(self.frame1, text='Medium', bg='medium sea green', fg='#0a4500', font=("comic sans ms", 13), variable=self.var, value=5, command=self.diffSelect)
        self.diffRbtn2.grid(column=1, row=1)
        self.diffRbtn3 = Radiobutton(self.frame1, text='Hard', bg='medium sea green', fg='#0a4500', font=("comic sans ms", 13), variable=self.var, value=6, command=self.diffSelect)
        self.diffRbtn3.grid(column=2, row=1)

        self.root.mainloop()
        
    def diffSelect(self):
        global diff
        self.playBtn.config(state=NORMAL)
        self.diff = self.var.get()
        print(self.diff)

    
    def play(self):
        global nextBtn, timeLb, pointsLb, heartsLb
        self.sec = 5
        self.points = 0
        self.btnlist = []
        self.colors = []
        self.done = []
        colorlist = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff', '#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff']
        colorlist1 = ['red', 'green', 'pink', 'purple', 'red', 'green', 'pink', 'purple']
        colorlist2 = ['mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey', 'mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey']
        if self.diff == 5:
            colorlist = colorlist + colorlist1
        elif self.diff == 6:
            colorlist = colorlist + colorlist1 + colorlist2
        self.playBtn.grid_remove()
        self.diffRbtn1.grid_remove()
        self.diffRbtn2.grid_remove()
        self.diffRbtn3.grid_remove()
        print(self.diff)
        
        for a in range(1,self.diff):
            for i in range(0,self.diff):
                color = choices(colorlist)
                name = 'btn'+str(i)+str(a)
                globals()['btn'+str(i)+str(a)] = Button(self.frame1, width=9, height=4, state=DISABLED, 
                                        bg=color, command=lambda b=color, n=name: self.choice(b,n))
                globals()['btn'+str(i)+str(a)].grid(column=i, row=a)
                self.btnlist.append('btn'+str(i)+str(a))
                colorlist.remove(str(color).replace("['", "").replace("']", ""))

        frame2 = Frame(self.frame1, bg='medium sea green', bd=5)
        frame2.grid(column=0, row=6, columnspan=4)

        self.heartsLb = Label(frame2, text=str(self.hearts)+"/5", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 11))
        self.heartsLb.grid(column=0, row=0)

        timeLb = Label(self.root, bg='medium sea green', font=("comic sans ms", 10))
        timeLb.grid(column=1, row=0)

        self.pointsLb = Label(frame2, text="Points: 0", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 11))
        self.pointsLb.grid(column=1, row=0)

        self.nextBtn = Button(self.frame1, text="Next level", bg='green yellow', fg='#0a4500', font=("comic sans ms", 10), width=8, height=1, state=DISABLED, command=self.play)
        self.nextBtn.grid(column=self.diff-1, row=6, columnspan=2)

        levelLb = Label(self.frame1, text='Level: '+str(self.level), bg='medium sea green', fg='#0a4500', font=("comic sans ms", 14)).grid(column=0, row=0, columnspan=2)

        if self.sec == 5:
            self.start()

    def start(self):
        global sec
        if self.sec > 0:
            timeLb.config(text=str(self.sec))
            timeLb.after(1000, self.start)
        else:
            for i in self.btnlist:
                globals()[str(i)].config(bg="white", state=NORMAL)
            timeLb.grid_remove()
        self.sec -= 1

    def choice(self,b,n):
        global points, hearts
        globals()[str(n)].config(bg=b, state=DISABLED)
        self.colors.append(b)
        self.done.append(n)

        if len(self.colors) == 2 and self.colors[0] == self.colors[1]:
            globals()[str(n)].config(state=DISABLED)
            self.colors.clear()
            self.points += 1
            self.pointsLb.config(text="Points: " + str(self.points))
        elif len(self.colors) == 2 and self.colors[0] != self.colors[1]:
            self.colors.clear()
            self.hearts -= 1
            self.heartsLb.config(text=str(self.hearts)+"/5")
            for i in self.done[-2:]:
                globals()[str(i)].config(bg="white", state=NORMAL)

        if self.hearts == 0:
            for i in self.btnlist:
                globals()[str(i)].config(state=DISABLED)
            #доделать! проигрыш в игре + кнопка для перехода на гл меню + шкала с кол-вом кнопок + ~темы
        
        if self.points == 6:
            self.levels()

    def levels(self):
        global level
        self.level += 1
        self.nextBtn.config(state=NORMAL)

if __name__ == '__main__':
    Game()