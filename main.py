import tkinter
from tkinter import ttk
import new_tab
tabs = []
def binding():
    tabs[-1].bind('<Expose>',on_add_tab)

def on_add_tab(event):
    tabs.append(ttk.Frame(main_window))
    main_window.add(tabs[-1],text='➕')
    current_tab = len(tabs) -2
    new_tab.new_Tab(tabs[current_tab])
    tabs[current_tab].unbind('<Expose>')
    main_window.tab(tabs[current_tab], text='New tab')
    binding()
root = tkinter.Tk()
main_window = ttk.Notebook(root)
main_window.pack(fill = 'both')
tabs.append(ttk.Frame(main_window))
main_window.add(tabs[0], text = 'New tab')
new_tab.new_Tab(tabs[0])
tabs.append(ttk.Frame(main_window))
main_window.add(tabs[1],text='➕')
binding()
root.mainloop()
# handle closing window