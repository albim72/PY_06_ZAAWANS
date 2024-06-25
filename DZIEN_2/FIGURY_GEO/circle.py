#napisz klasę Circle, po jednym parametrze: promień - a, opartą na klasie Figure()
#policz pole koła dla promienia 5.5

from figura import Figure
import math

class Circle(Figure):
    def __init__(self, a):
        super().__init__(a)

    def calc_area(self):
        return math.pi*self.a**2

    # def print_b(self):
    #     if self.b:
    #         return self.b
