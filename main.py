from tkinter import *
from tkinter import messagebox
from random import choices


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

        self.lidersBtn = Button(self.frame1, text="Leaders", width=8, height=1, bg='green yellow', fg='#0a4500', font=("comic sans ms", 25))
        self.lidersBtn.grid(column=0, row=2, columnspan=3)

        self.root.mainloop()
        
    def diffSelect(self):
        global diff
        self.playBtn.config(state=NORMAL)
        self.diff = self.var.get()
    
    def play(self):
        global nextBtn, timeLb, pointsLb, heartsLb
        self.sec = self.diff + 2
        self.points = 0
        self.btnlist = []
        self.colors = []
        self.done = []
        colorlist = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff', '#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff']
        colorlist1 = ['#1ca9c9', 'green', 'pink', 'purple', '#1ca9c9', 'green', 'pink', 'purple']
        colorlist2 = ['mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey', 'mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey']
        if self.diff == 5:
            colorlist = colorlist + colorlist1
        elif self.diff == 6:
            colorlist = colorlist + colorlist1 + colorlist2
        self.playBtn.grid_remove()
        self.lidersBtn.grid_remove()
        self.diffRbtn1.grid_remove()
        self.diffRbtn2.grid_remove()
        self.diffRbtn3.grid_remove()
        
        for a in range(1,self.diff):
            for i in range(0,self.diff):
                color = choices(colorlist)
                name = 'btn'+str(i)+str(a)
                globals()['btn'+str(i)+str(a)] = Button(self.frame1, width=9, height=4, state=DISABLED, 
                                        bg=color, command=lambda b=color, n=name: self.choice(b,n))
                globals()['btn'+str(i)+str(a)].grid(column=i, row=a)
                self.btnlist.append('btn'+str(i)+str(a))
                colorlist.remove(str(color).replace("['", "").replace("']", ""))
        
        if self.level > 1:
            self.heartsLb.grid_remove()

        self.heartsLb = Label(self.frame1, text="❤"*self.hearts, bg='medium sea green', fg='#0a4500', font=("comic sans ms", 13))
        self.heartsLb.grid(column=0, row=7, columnspan=3)

        timeLb = Label(self.frame1, bg='medium sea green', fg='#0a4500', font=("comic sans ms", 12))
        timeLb.grid(column=self.diff-1, row=0)

        self.pointsLb = Label(self.frame1, text="Points: 0", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 13))
        self.pointsLb.grid(column=0, row=6, columnspan=3)

        self.nextBtn = Button(self.frame1, text="Next level", bg='green yellow', fg='#0a4500', font=("comic sans ms", 10), width=8, height=1, state=DISABLED, command=self.play)
        self.nextBtn.grid(column=self.diff-1, row=6, columnspan=2)

        levelLb = Label(self.frame1, text='Level: '+str(self.level), bg='medium sea green', fg='#0a4500', font=("comic sans ms", 14)).grid(column=0, row=0, columnspan=2)

        if self.sec == self.diff + 2:
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
            self.heartsLb.config(text="❤"*self.hearts)
            for i in self.done[-2:]:
                globals()[str(i)].config(bg="white", state=NORMAL)

        if self.hearts == 0:
            for i in self.btnlist:
                globals()[str(i)].config(state=DISABLED)
            self.window = Toplevel()
            self.window.geometry(f'350x300+{self.window.winfo_screenwidth()//2 - 178}+{self.window.winfo_screenheight()//2 - 178}')
            self.window["bg"] = "medium sea green"
            title = Label(self.window, text="Game ower", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 30))
            title.pack()
            nameLb = Label(self.window, text="Your name:", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 15))
            nameLb.pack()
            self.nickname=Text(self.window, height=2, width=15, font='Arial 14', wrap=WORD)
            self.nickname.pack()
            recordLb = Label(self.window, text="Your record:", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 15))
            recordLb.pack()
            recordlLb = Label(self.window, text="Level: " + str(self.level), bg='medium sea green', fg='#0a4500', font=("comic sans ms", 15))
            recordlLb.pack()
            menuBtn = Button(self.window, text="Back", width=7, height=1, bg='medium sea green', fg='#0a4500', font=("comic sans ms", 20), command=self.records)
            menuBtn.pack()
            
            
            
            #доделать! проигрыш в игре + кнопка для перехода на гл меню
        
        if self.points == 6:
            self.levels()

    def levels(self):
        global level
        self.level += 1
        
        self.nextBtn.config(state=NORMAL)

    def records(self):
        nick = self.nickname.get('1.0', END)
        print(nick)
        record = self.level
        print(record)
        self.window.destroy()
        

if __name__ == '__main__':
    Game()