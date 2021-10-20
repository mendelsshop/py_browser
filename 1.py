import tkinter as tk
from tkinter import ttk
root = tk.Tk()
i = {}
c = 0
def hello(event):
    global c
    global i
    c += 1
    i[c] = ttk.Frame(root)
    print(i[c])
    mainwindow.add(i[c], text =f'{c}')
mainwindow = ttk.Notebook(root)
maintab = ttk.Frame(root)
random_text = ttk.Label(maintab,text='the brown fox jumped over the lazy dog').pack()
mainwindow.add(maintab,text='tab1')
secondtab = ttk.Frame(root)
random_text_1 = ttk.Label(secondtab,text='the brown fox jumped over the lazy dog').pack()
random_text_2 = ttk.Label(secondtab,text='lttstore.com').pack()
secondtab.bind('<Expose>',hello)
mainwindow.add(secondtab,text='tab2')
print(mainwindow.tabs())
mainwindow.pack()
root.mainloop()