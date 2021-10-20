import tkinter
from tkinter import ttk
import new_tab

def on_add_tab():
    print('h')
root = tkinter.Tk()
main_window = ttk.Notebook(root)
main_window.pack(fill = 'both')
tab_1 = ttk.Frame(main_window)
main_window.add(tab_1, text = 'New tab')
new_tab.new_Tab(tab_1)
add_tab = ttk.Frame(main_window)
main_window.add(add_tab,text='➕')
add_tab.bind('<FocusIn>',on_add_tab())
root.mainloop()
