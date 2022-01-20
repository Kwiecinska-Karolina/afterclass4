class Ebook():
    def __init__(self, title, author, number_of_pages, current_page):
        self.is_open=False
        self.title=title
        self.author=author
        self.number_of_pages=number_of_pages
        self.current_page=current_page
    def close_ebook(self):
        self.is_open=False
        print(f'Książka jest zamknięta')
    def open_ebook(self):
        self.is_open=True
        self.current_page=1
    def next_page(self):
        self.current_page+=1
    def previous_page(self):
        self.current_page-=1
    def ebook_status(self):
        if( self.current_page)> 0 and (self.current_page<self.number_of_pages) and (self.is_open==True):
            print(f'Book \nTitle: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.number_of_pages}\nCurrent page: {self.current_page}')
        else:
            print(f'Open a book')
 
