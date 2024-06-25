from figura import Figure
from square import Square

class Rectangle(Figure):
    def __new__(cls,a,b):
        if a==b:
            return Square(side=a)
        return object.__new__(Rectangle)
    
    def calc_area(self):
        return self.a*self.b
