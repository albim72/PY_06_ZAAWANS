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
        print(f"Testowy {self.name}, informacje: {self.issue}")
    
        
    
    
