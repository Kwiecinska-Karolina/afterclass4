class Book():
    def __init__(self,title,author,number_of_pages):
        self.title=title
        self.author=author
        self.number_of_pages=number_of_pages
        
    def show_book(self):
        print(f'{self.title} {self.author } {self.number_of_pages }')
        
class E_book(Book):
    def __init__(self,title,author,number_of_pages,file_name):
        self.file_name=file_name
        super().__init__(title,author,number_of_pages)
    def show_book(self):
        print(f'{self.title} {self.author } {self.number_of_pages } {self.file_name}')
   
b1=Book("Nigdy","Ken Follett",736)
eb1=E_book("Białośnieżka i Różanka", "Jacob i Wilhelm Grimm", 10,"https://wolnelektury.pl/katalog/lektura/bialosniezka-i-rozanka.html")
eb1.show_book()
b1.show_book()