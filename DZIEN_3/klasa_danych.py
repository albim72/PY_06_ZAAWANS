from dataclasses import dataclass

class Number:
    def __init__(self,x):
        self.x=x

zb = Number(5)
print(zb.x)

print("klasa danych....")

@dataclass
class DatNumber:
    y: float
    x:int = 10


db = DatNumber(2.345,7)
print(db)
print(db.x)

db2 = DatNumber(True)
print(db2.x)
print(db2.y)

class Reg:
    x:int = 1
    y:int = 2
    z:int = 4

r = Reg()
print(r.x)

print("_"*50)
@dataclass
class Dane:
    nazwa:str
    licznik:int=0
    cena:float=0.0

    @property
    def licznik(self):
        return self._licznik

    @licznik.setter
    def licznik(self,n_1):
        self._licznik = n_1

p = Dane("pudełko",4,11.2)
print(f'produkt: {p.nazwa} -> cena: {p.cena} zł -> zapłata: {p.cena*p.licznik} zł')

p.licznik = 16

print(f'produkt: {p.nazwa} -> cena: {p.cena} zł -> zapłata: {p.cena*p.licznik} zł')
