from cefpython3 import cefpython as cef
import tkinter
from tkinter import ttk
import bookmark
root = tkinter.Tk()
main_window = ttk.Notebook(root)
main_window.pack(fill = 'both')
default_tab = ttk.Frame(main_window)
main_window.add(default_tab, text = 'New tab')
search_box = ttk.Entry(default_tab)
search_box.grid()
bookmark_bar = ttk.Frame(default_tab)
bookmark_bar.grid(row = 1)
bookmarks = bookmark.bookmark_handler()
for name , url in bookmarks.items():
    bookmark_tuple = (name,url)
    name = bookmark.Bookmark(bookmark_tuple)
    print(name.name)
    name.button = ttk.Button(bookmark_bar,text=name.name)
    name.button.grid(row =0)
browser = cef.CreateBrowserSync(default_tab, url="https://www.google.com/")
assert browser
root.mainloop()