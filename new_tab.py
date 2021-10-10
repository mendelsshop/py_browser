import tkinter
from tkinter import ttk
import bookmark
import threading
from cefpython3 import cefpython as cef
import sys
class new_Tab():
    def __init__(self, frame):
        self.frame = frame
        self.searchBar = ttk.Frame(self.frame)
        self.back = ttk.Button(self.searchBar,text='⬅️')
        self.back.grid(row=0, column=0)
        self.back = ttk.Button(self.searchBar,text='➡️')
        self.back.grid(row=0, column=1)
        self.back = ttk.Button(self.searchBar,text='🔄️')
        self.back.grid(row=0, column=2)
        self.back = ttk.Button(self.searchBar,text='Home')
        self.back.grid(row=0, column=3)
        self.search_box = ttk.Entry(self.searchBar)
        self.search_box.grid(row=0,column=4)
        self.search = ttk.Button(self.searchBar,text='🔍')
        self.search.grid(row=0,column=5)
        self.searchBar.grid(row=0,sticky='we')
        self.bookmark_bar = ttk.Frame(self.frame)
        self.bookmark_bar.grid(row = 1,sticky='we')
        self.bookmarks = bookmark.bookmark_handler()
        counter = 0
        for name , url in self.bookmarks.items():
            bookmark_tuple = (name,url)
            name = bookmark.Bookmark(bookmark_tuple)
            name.button = ttk.Button(self.bookmark_bar,text=name.name)
            name.button.grid(row =0,column=counter)
            counter +=1
        self.browserframe = ttk.Frame(self.frame,height=800,width=800)
        self.browserframe.grid(row =3)
        self.rect = [0, 0, 800, 800]
        self.thread = threading.Thread(target=self.test_thread)
        self.thread.start()
        print('browser: ', self.rect[2], 'x', self.rect[3])

    def test_thread(self):
        sys.excepthook = cef.ExceptHook
        self.window_info = cef.WindowInfo()
        self.window_info.SetAsChild(self.browserframe.winfo_id(),self.rect)
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(self.window_info, url="https://www.google.com/")
        cef.MessageLoop()
