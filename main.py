import tkinter
from tkinter import ttk
import bookmark
root = tkinter.Tk()
main_window = ttk.Notebook(root)
main_window.pack(fill = 'both')
default_tab = ttk.Frame(main_window)
main_window.add(default_tab, text = 'New tab')
bookmark_bar = ttk.Frame(default_tab)
bookmark_bar.grid(row = 0)
bookmarks = bookmark.bookmark_handler()
for name , url in bookmarks.items():
    bookmark_tuple = (name,url)
    name = bookmark.Bookmark(bookmark_tuple)
    print(name.name)
    name.button = ttk.Button(bookmark_bar,text=name.name)
    name.button.grid(row =0)
root.mainloop()