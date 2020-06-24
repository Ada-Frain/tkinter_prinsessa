from tkinter import *
from tkinter import ttk
from random import choices


level = 1
sec = 4
points = 0
hearts = 5
colors = []
done = []
btnlist = []
colorlist = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff', '#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff']


def levels():
    global sec, colorlist, level, points
    points = 0
    sec = 4
    colorlist = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff', '#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#0000ff', '#7d00ff']
    level += 1
    nextBtn.config(state=NORMAL)


def choice(b,n):
    global points, hearts
    globals()[str(n)].config(bg=b, state=DISABLED)
    colors.append(b)
    done.append(n)
    if len(colors) == 2 and colors[0] == colors[1]:
        globals()[str(n)].config(state=DISABLED)
        colors.clear()
        points += 1
        pointsLb.config(text="Points: " + str(points))
    elif len(colors) == 2 and colors[0] != colors[1]:
        colors.clear()
        hearts -= 1
        heartsLb.config(text=str(hearts)+"/5")
        for i in done[-2:]:
            globals()[str(i)].config(bg="white", state=NORMAL)

    if hearts == 0:
        playBtn.grid(column=0, row=0)
    
    if points == 6:
        levels()

    
def start():
    global sec
    if sec > 0:
        timeLb.config(text=str(sec))
        timeLb.after(1000, start)
    else:
        for i in btnlist:
            globals()[str(i)].config(bg="white", state=NORMAL)
        timeLb.config(text="")
    sec -= 1


def play():
    global nextBtn, timeLb, pointsLb, heartsLb
    playBtn.grid_remove()
    diffSc.grid_remove()

    for a in range(1,4):
        for i in range(0,4):
            color = choices(colorlist)
            name = 'btn'+str(i)+str(a)
            globals()['btn'+str(i)+str(a)] = Button(frame1, width=9, height=4, state=DISABLED, 
                                    bg=color, command=lambda b=color, n=name: choice(b,n))
            globals()['btn'+str(i)+str(a)].grid(column=i, row=a)
            btnlist.append('btn'+str(i)+str(a))
            colorlist.remove(str(color).replace("['", "").replace("']", ""))

    heartsLb = Label(frame1, text=str(hearts)+"/5", bg='medium sea green', font=("comic sans ms", 10))
    heartsLb.grid(column=0, row=0)
    timeLb = Label(frame1, bg='medium sea green', font=("comic sans ms", 10))
    timeLb.grid(column=0, row=5)
    pointsLb = Label(frame1, text="Points: 0", bg='medium sea green', font=("comic sans ms", 10))
    pointsLb.grid(column=1, row=5)
    nextBtn = Button(frame1, text="Next level", bg='green yellow', font=("comic sans ms", 10), state=DISABLED, command=play)
    nextBtn.grid(column=3, row=5)
    levelLb = Label(frame1, text='Level: '+str(level), bg='medium sea green', font=("comic sans ms", 10)).grid(column=2, row=5)

    if sec == 4:
        start()


root = Tk()
root.title("Игра")
root.geometry(f'600x550+{root.winfo_screenwidth()//2 - 300}+{root.winfo_screenheight()//2 - 300}')
root["bg"] = "medium sea green"
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame1 = Frame(root, bg='medium sea green', bd=5)
frame1.grid(column=0, row=0)

playBtn = Button(frame1, text="Play!", width=7, height=1, bg='green yellow', fg='red', font=("comic sans ms", 30), command=play)
playBtn.grid(column=0, row=0)

diffSc = Scale(frame1, orient=HORIZONTAL, length=250, from_=1, to=2, tickinterval=1, resolution=1, font=("comic sans ms", 10))
diffSc.grid(column=0, row=1)
diff = diffSc.get()

window = Toplevel()
window.geometry('350x300')
window["bg"] = "medium sea green"
title = Label(window, text="Game ower", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 30))
title.pack()
nameLb = Label(window, text="Your name:", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 15))
nameLb.pack()
nikname=Text(window, height=2, width=15, font='Arial 14', wrap=WORD)
nikname.pack()
recordLb = Label(window, text="Your record:", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 15))
recordLb.pack()
recordlLb = Label(window, text="", bg='medium sea green', fg='#0a4500', font=("comic sans ms", 15))
recordlLb.pack()
menuBtn = Button(window, text="Back", width=7, height=1, bg='medium sea green', fg='#0a4500', font=("comic sans ms", 20))
menuBtn.pack()
root.mainloop()