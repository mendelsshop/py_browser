from cefpython3 import cefpython as cef
import tkinter
from tkinter import ttk
import bookmark
import sys
import threading
def test_thread(browserframe):
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo()
    window_info.SetAsChild(browserframe.winfo_id(),rect)
    cef.Initialize()
    browser = cef.CreateBrowserSync(window_info, url="https://www.google.com/")
    cef.MessageLoop()
root = tkinter.Tk()

main_window = ttk.Notebook(root)
main_window.pack(fill = 'both')
default_tab = ttk.Frame(main_window)
main_window.add(default_tab, text = 'New tab')
search_box = ttk.Entry(default_tab)
search_box.grid(row=0)
bookmark_bar = ttk.Frame(default_tab)
bookmark_bar.grid(row = 1)
bookmarks = bookmark.bookmark_handler()
counter = 0
for name , url in bookmarks.items():
    bookmark_tuple = (name,url)
    name = bookmark.Bookmark(bookmark_tuple)
    name.button = ttk.Button(bookmark_bar,text=name.name)
    name.button.grid(row =0,column=counter)
    counter +=1
browserframe = ttk.Frame(default_tab,height=800,width=800)
browserframe.grid(row =3)
rect = [0, 0, 800, 800]
thread = threading.Thread(target=test_thread, args=(browserframe,))
thread.start()
print('browser: ', rect[2], 'x', rect[3])
root.mainloop()
