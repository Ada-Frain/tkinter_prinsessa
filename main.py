from tkinter import *
from random import choices


class Game():
    def __init__(self):
        self.root = Tk()
        self.root.geometry(f'600x550+{self.root.winfo_screenwidth()//2 - 300}+{self.root.winfo_screenheight()//2 - 300}')
        self.root.title("АльцГеймер")

        self.root["bg"] = "medium sea green"
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.frame1 = Frame(self.root, bg='medium sea green', bd=5)
        self.frame1.grid(column=0, row=0)

        self.playBtn = Button(self.frame1, text="Play!", width=7, height=1, bg='green yellow', fg='red', font=("comic sans ms", 30), command=self.play)
        self.playBtn.grid(column=0, row=0)

        self.diffSc = Scale(self.frame1, orient=HORIZONTAL, length=250, from_=1, to=2, tickinterval=1, resolution=1, font=("comic sans ms", 10))
        self.diffSc.grid(column=0, row=1)
        diff = self.diffSc.get()


        self.root.mainloop()
    
    def play(self):
        global nextBtn, timeLb, pointsLb, heartsLb
        self.level = 1
        self.sec = 4
        self.points = 0
        self.hearts = 5
        self.btnlist = []
        self.colors = []
        self.done = []
        colorlist = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff', '#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff']
        self.playBtn.grid_remove()
        self.diffSc.grid_remove()
        
        for a in range(1,4):
            for i in range(0,4):
                color = choices(colorlist)
                name = 'btn'+str(i)+str(a)
                globals()['btn'+str(i)+str(a)] = Button(self.frame1, width=9, height=4, state=DISABLED, 
                                        bg=color, command=lambda b=color, n=name: self.choice(b,n))
                globals()['btn'+str(i)+str(a)].grid(column=i, row=a)
                self.btnlist.append('btn'+str(i)+str(a))
                colorlist.remove(str(color).replace("['", "").replace("']", ""))

        self.heartsLb = Label(self.frame1, text=str(self.hearts)+"/5", bg='medium sea green', font=("comic sans ms", 10))
        self.heartsLb.grid(column=0, row=0)
        timeLb = Label(self.frame1, bg='medium sea green', font=("comic sans ms", 10))
        timeLb.grid(column=0, row=5)
        self.pointsLb = Label(self.frame1, text="Points: 0", bg='medium sea green', font=("comic sans ms", 10))
        self.pointsLb.grid(column=1, row=5)
        self.nextBtn = Button(self.frame1, text="Next level", bg='green yellow', font=("comic sans ms", 10), state=DISABLED, command=self.play)
        self.nextBtn.grid(column=3, row=5)
        levelLb = Label(self.frame1, text='Level: '+str(self.level), bg='medium sea green', font=("comic sans ms", 10)).grid(column=2, row=5)

        if self.sec == 4:
            self.start()

    def start(self):
        global sec
        if self.sec > 0:
            timeLb.config(text=str(self.sec))
            timeLb.after(1000, self.start)
        else:
            for i in self.btnlist:
                globals()[str(i)].config(bg="white", state=NORMAL)
            timeLb.config(text="")
        self.sec -= 1

    def choice(self,b,n):
        global points, hearts
        globals()[str(n)].config(bg=b, state=DISABLED)
        self.colors.append(b)
        self.done.append(n)
        # print(colors, done)
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
            self.playBtn.grid(column=0, row=0)
        
        if self.points == 6:
            self.levels()

    def levels(self):
        global sec, colorlist, level, points
        self.points = 0
        self.sec = 4
        colorlist = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff', '#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff']
        self.level += 1
        self.nextBtn.config(state=NORMAL)

if __name__ == '__main__':
    Game()