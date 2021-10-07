import tkinter
from tkinter import ttk
def bookmark_handler():
    with open('bookmarks.txt' , 'rt') as bookmark_file:
        bookmarks = {}
        for line in bookmark_file:
            tuple = line.split('http')
            tuple[0] = tuple[0].strip()
            tuple[1] = 'http'+tuple[1]
            bookmarks[tuple[0]] = tuple[1]
    return bookmarks
            
class Bookmark:
    def __init__(self, bookmark_from_dict):
        self.url = bookmark_from_dict[1]
        self.name = bookmark_from_dict[0]
        self.button = None
    def __str__(self):
        return self.name
