import tkinter
from tkinter import ttk
def bookmark():
    bookmarks = ['bookmark', 'potato kugel']

    bookmark_counters = 0
    bookmarkss = {}
    for bookmark_name in bookmarks:
        bookmarkss[f'bookmark_{bookmark_counters}']=ttk.Button(bookmark_bar,text=bookmark_name).grid(column = bookmark_counters, row=0)
        bookmark_counters += 1