from tkinter import *
from tkinter import ttk
from random import choices

level = 1
sec = 4
points = 0
colors = []
done = []
btnlist = []
colorlist = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'red', 'blue', 'green', 'purple', 'orange', 'yellow']


def levels():
    global sec, colorlist, level, points
    points = 0
    sec = 4
    colorlist = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'red', 'blue', 'green', 'purple', 'orange', 'yellow']
    level += 1
    nextBtn = Button(root, text="Next", command=play).grid(column=0, row=6)

def choice(b,n):
    global points
    globals()[str(n)].config(bg=b, state=DISABLED)
    colors.append(b)
    done.append(n)
    if len(colors) == 2 and colors[0] == colors[1]:
        globals()[str(n)].config(state=DISABLED)
        colors.clear()
        done.append(str(n))
        points += 1
        pointsLb.config(text="Points: " + str(points))
    elif len(colors) == 2 and colors[0] != colors[1]:
        colors.clear() 
        for i in done[-2:]:
            globals()[str(i)].config(bg="white", state=NORMAL)
    
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
        timeLb.config(text="Play!")
    sec -= 1


def play():
    playBtn.grid_remove()
    root.grid_rowconfigure(0, weight=0)
    root.grid_columnconfigure(0, weight=0)
    for a in range(0,3):
        for i in range(0,4):
            globals()['btn'+str(i)+str(a)] = Button(root, width=9, height=4, state=DISABLED)
            color = choices(colorlist)
            name = 'btn'+str(i)+str(a)
            globals()['btn'+str(i)+str(a)].config(bg=color, command=lambda b=color, n=name: choice(b,n))
            globals()['btn'+str(i)+str(a)].grid(column=i, row=a)
            btnlist.append('btn'+str(i)+str(a))
            colorlist.remove(str(color).replace("['", "").replace("']", ""))

    pointsLb.config(text="Points: 0")

    if sec == 4:
        start()

root = Tk()
root.title("Игра")
root.geometry('600x550')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

playBtn = Button(root, text="Play!", width=25, height=5, bg='black', fg='red', font='arial 14', command=play)
playBtn.grid(column=0, row=0)

timeLb = Label(root, font=("gabriola", 15))
timeLb.grid(column=0, row=5)

pointsLb = Label(root, font=("gabriola", 15))
pointsLb.grid(column=1, row=5)

root.mainloop()