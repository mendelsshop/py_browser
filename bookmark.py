def bookmark_handler():
    with open('bookmarks.txt' , 'rt') as bookmark_file:
        bookmarks = {}
        for line in bookmark_file:
            tuple = line.split('http')
            tuple[0] = tuple[0].strip()
            tuple[1] = 'http'+tuple[1]
            bookmarks[tuple[0]] = tuple[1]
    return bookmarks
            
def bookmarks_opener():
    