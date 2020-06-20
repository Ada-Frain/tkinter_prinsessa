from tkinter import *
from random import choices

sec = 4
colors = []
done = []
points = 0
colorlist = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'red', 'blue', 'green', 'purple', 'orange', 'yellow']
list = []


def choice(b,n):
    global points
    globals()[str(n)].config(bg=b, state=DISABLED)
    colors.append(b)
    done.append(n)
    # print(colors)
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
    
    print(done)
    

def start():
    global sec
    if sec > 0:
        timeLb.config(text=str(sec))
        timeLb.after(1000, start)
    else:
        for i in list:
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
            list.append('btn'+str(i)+str(a))
            # colorlist.remove(str(color))

    pointsLb.config(text="Points: 0")

    if sec == 4:
        start()

root = Tk()
root.title("Игра")
root.geometry('700x600')

playBtn = Button(root, text="Play!", command=play).grid(column=0, row=0)

timeLb = Label(root, font=("gabriola", 30))
timeLb.grid(column=4, row=0)

pointsLb = Label(root, font=("gabriola", 30))
pointsLb.grid(column=5, row=0)

root.mainloop()

