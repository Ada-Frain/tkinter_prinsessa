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


def choice(b,n):
    global points, level
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
    for a in range(1,4):
        for i in range(1,5):
            globals()['btn'+str(i)+str(a)] = Button(root, width=13, height=6, state=DISABLED)
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

playBtn = Button(root, text="Play!", command=play).grid(column=2, row=2)

timeLb = Label(root, font=("gabriola", 25))
timeLb.grid(column=1, row=0)

pointsLb = Label(root, font=("gabriola", 25))
pointsLb.grid(column=2, row=0)

root.mainloop()