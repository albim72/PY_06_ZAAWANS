class Book:
    def __init__(self,title,author,price,pages,bookstore_nb):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.bookstore_nb = bookstore_nb
        self.binding = "soft"
        
    def __repr__(self):
        return f'Książka - {self.title}, cena -> {self.price} zł'
