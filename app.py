from tkinter import *
from tkinter import scrolledtext, messagebox, ttk, filedialog, Menu
from tkinter.ttk import Combobox, Checkbutton, Radiobutton, Progressbar, Notebook, Frame
from os import path

def clicked():
    res = "Hello {}!".format(txt.get())
    lbl.configure(text=res)

def clickrad1():
    res = "{} are lovely.".format(txt.get())
    lbl1.configure(text=res)

def clickrad2():
    res = "{} are bad guy.".format(txt.get())
    lbl1.configure(text=res)

def clickrad3():
    res = "{} are idiot.".format(txt.get())
    lbl1.configure(text=res)

def combodef():
    res = combo.get()
    lbl1.configure(text=res)

def radiodef():
    lblradio.configure(text=selected.get())

def delete():
    txt1.delete(1.0, END)

def message():
    messagebox.showinfo('Слова на русском', 'Первые и последние.')

def messageask():
    res = messagebox.askquestion('Ты кто?', 'Внимательно подумай!') # askyesno, askyesnocancel(три значения), askokcancel, askretrycancel 

def filedef():
    file = filedialog.askopenfilename(initialdir= path.dirname(__file__))

# Создание окна
window = Tk()
window.title("Добро пожаловать!")
window.geometry('700x500')
# виджет Label и его позиция в окне с помощью функции grid
lbl = Label(window, text="Hello!", font=("gabriola", 15), fg="purple")
lbl.grid(column=0, row=0)
# Поле ввода, можно также отключить виджет - state='disabled'
txt = Entry(window, width=20)
txt.grid(column=1, row=0)
txt.focus()
# Добавление кнопки и функции к ней
btn = Button(window, text="Don't touch!", command=clicked,
            fg="pink", bg="brown", font=("gabriola", 15))
btn.grid(column=2, row=0)
# Виджет поля с выпадающим списком
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(0) # значение по умолчанию
combo.grid(column=0, row=1)
btn1 = Button(window, text='test', command=combodef)
btn1.grid(column=1, row=1)
# Создание чекбокса, var=chk_state - значение по умолчанию
chk_state = BooleanVar()
chk_state.set(True) #проверка состояния чекбокса
chk = Checkbutton(window, text='Select', var=chk_state)
chk.grid(column=2, row=1)
# Виджеты Radio Button и функции, которые исполняются сразу после выбора
rad1 = Radiobutton(window, text='First', value=1, command=clickrad1)
rad2 = Radiobutton(window, text='Second', value=2, command=clickrad2)
rad3 = Radiobutton(window, text='Third', value=3, command=clickrad3)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)
lbl1 = Label(window, text="Who are you?", font=("gabriola", 15), fg="purple")
lbl1.grid(column=0, row=3)
# Radio Button с кнопкой
selected = IntVar() # тоже самое, что и BooleanVar()
radb1 = Radiobutton(window, text='First', value=1, variable=selected)
radb2 = Radiobutton(window, text='Second', value=2, variable=selected)
radb3 = Radiobutton(window, text='Third', value=3, variable=selected)
radb1.grid(column=0, row=4)
radb2.grid(column=1, row=4)
radb3.grid(column=2, row=4)
btnradio = Button(window, text="radio", command=radiodef)
btnradio.grid(column=3, row=4)
lblradio = Label(window, text="Who are you?", font=("gabriola", 15), fg="purple")
lblradio.grid(column=4, row=4)
# Текстовая область
txt1 = scrolledtext.ScrolledText(window, width=10, height=10)
txt1.insert(INSERT, 'F') # настроить содержимое
txt1.grid(column=0, row=5)
btn2 = Button(window, text='delete', command=delete)
btn2.grid(column=1, row=5)
# Всплывающее окно (messagebox.showwarning показывает предупреждающее сообщение, .showerror сообщение об ошибке)
btn3 = Button(window, text='Click', command=message) # Эта кнопка вызывает функцию с messagebox.showinfo
btn3.grid(column=2, row=5)
# Диалоговое окно с выбором варианта
btn4 = Button(window, text='Click2', command=messageask) # Эта кнопка вызывает функцию с messagebox.askquestion
btn4.grid(column=3, row=5)
# Создание виджета спинбокса
var = IntVar()
var.set(36) # Значение по умочанию
spin = Spinbox(window, from_=0, to=100, width=5) # вместо "from_=0, to=100" можно указать несколько чисел "values=(3, 8, 11)"
spin.grid(column=4, row=5)
# Добавление виджета Progressbar
bar = Progressbar(window, length=200)
bar['value'] = 70 # Установите значение progressbar
# Изменение цвета Progressbar. Сначала нужно создать стиль и задать цвет фона, а затем настроить созданный стиль на Progressbar.
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar1 = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar1['value'] = 70
bar1.grid(column=0, row=6)
# Добавление поля загрузки файла, для этого стоит создать функцию. filetypes - указание типов файла
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*"))) # Можно запросить несколько файлов - filedialog.askopenfilenames()
# dir = filedialog.askdirectory() # Можно запросить каталог
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__)) # Можно указать начальную директорию для диалогового окна файла
btn5 = Button(window, text='File', command=filedef)
btn5.grid(column=1, row=6)
# Добавление панели меню и пунктов подменю
menu = Menu(window)
new_item = Menu(menu, tearoff=0) # tearoff=0 - чтобы убрать пунkтирную линию в начале
new_item.add_command(label='New', command=filedef)
new_item.add_separator() # Разделяющая линия
new_item.add_command(label='Change')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
# Вкладки. Для начала, создается элемент управления вкладкой, с помощью класса Notebook .
# Создайте вкладку, используя класс Frame.
# Добавьте эту вкладку в элемент управления вкладками.
# Запакуйте элемент управления вкладкой, чтобы он стал видимым в окне.
# tab_control = ttk.Notebook(window)  
# tab1 = ttk.Frame(tab_control)  
# tab_control.add(tab1, text='Первая')  
# tab_control.pack(expand=1, fill='both')
# Чтобы оно заработало надо в настройках каждого виджета указать, к какой вкладке он принадлежит (вместо 'windows')

# Добавление интервала для виджетов - Передайте padx и pady любому виджету и задайте значение.
# lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)

window.mainloop()