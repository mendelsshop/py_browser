import tkinter
from tkinter import ttk
import new_tab
root = tkinter.Tk()
main_window = ttk.Notebook(root)
main_window.pack(fill = 'both')
default_tab = ttk.Frame(main_window)
main_window.add(default_tab, text = 'New tab')
new_tab.new_Tab(default_tab)
root.mainloop()
