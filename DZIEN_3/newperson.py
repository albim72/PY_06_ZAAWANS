from dataclasses import dataclass,astuple,asdict,field
import datetime

@dataclass
class Person:
    city:str
    year:int = field(init=False)
    firstname:str = "Janek"
    lastname:str = "Kot"
    age:int = 30
    job:str = "Data developer"
    full_name:str = field(default=age,init=False,repr=False)

    def __repr__(self):
        return f"Pracownik: {self.firstname} {self.lastname}, stanowisko: {self.job}"
    def __str__(self):
        return (f"dane osoby....\n"
                f"{self.full_name}\n"
                f"rok urodzenia: {self.year}")
    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.year = datetime.datetime.now().year - self.age


os1 = Person("Kraków")
print(os1)
os1.firstname = "Jerzy"
print(os1.firstname)

os2 = Person("Kielce","Leon","Kos",45,"elektryk")
print(os2)

print(type(os2.full_name))
print(astuple(os1))
print(asdict(os2))
