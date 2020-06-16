from tkinter import *
from random import choices

colors = []
def choice(b,n):
    # global globals()[str(n)]

    globals()[str(n)].config(bg=b)
    colors.append(b)
    if colors[0] == colors[1]:
        lb1.config(text="Good")
    else:
        lb1.config(text="Bad")
    print(b, n)
    print(colors)

sec = 3 
def start():
    global sec
    
    # list = ['btn11', 'btn21', 'btn31', 'btn12', 'btn22', 'btn32', 'btn13', 'btn23', 'btn33']
    if sec > 0:
        lb1.config(text=str(sec))
        window.after(1000, start)
    else:
        for i in list:
            globals()[str(i)].config(bg="white")
        lb1.config(text="Time over")
    sec -= 1


window = Tk()
window.title("Игра")
window.geometry('700x780')

colorlist = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']
list = []
for a in range(1,4):
    for i in range(1,5):
        globals()['btn'+str(i)+str(a)] = Button(window, width=15, height=7)
        color = choices(colorlist)
        name = 'btn'+str(i)+str(a)
        globals()['btn'+str(i)+str(a)].config(bg=color, command=lambda b=color, n=name: choice(b,n))
        globals()['btn'+str(i)+str(a)].grid(column=i, row=a)
        list.append('btn'+str(i)+str(a))

lb1 = Label(window, text=str(sec), font=("gabriola", 30))
lb1.grid(column=4, row=0)

start()

window.mainloop()