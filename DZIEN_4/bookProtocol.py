from typing import Protocol

#definicja protokołu
class Printable(Protocol):
    def print_info(self)->None:
        pass

#klasa inmplementująca protokół
class Book(Printable):
    def __init__(self,title:str,author:str)->None:
        self.title = title
        self.author = author

    def print_info(self) -> None:
        print(f"Książka {self.title}, autor: {self.author}")

#druga klasa implemenetująca protokół
class Magazine(Printable):
    def __init__(self,name:str,issue:str)->None:
        self.name = name
        self.issue = issue

    def print_info(self) -> None:
        print(f"Magazyn {self.name}, wydanie: {self.issue}")


class Test:
    def __init__(self,name:str,info:str)->None:
        self.name = name
        self.info = info

    def print_info(self) -> None:
        print(f"Testowy {self.name}, informacje: {self.info}")

#funkcja, która przyjmuje obiekty zgodne z protokołem Printable
def print_details(item:Printable)->None:
    item.print_info()


book = Book("Hobbit","J.R.R. Tolkien")
magazine = Magazine("Skarby historii",'44')
print_details(book)
print_details(magazine)

print("wywołanie obiektu niezgodnego z protokołem Printable...")
tst = Test("materiały xyz","wariant 4")
print_details(tst)
