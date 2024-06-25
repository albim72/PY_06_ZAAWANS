from triangle import Triangle
from rectangle import Rectangle
from trapeze import Trapeze
from circle import Circle

tr = Triangle(5.6,7.2)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.calc_area()} cm2')

rc1 = Rectangle(4,5.8)
print(f'pole figury {rc1.__class__.__name__} wynosi: {rc1.calc_area()} cm2')

rc2 = Rectangle(5.5,5.5)
print(f'pole figury {rc2.__class__.__name__} wynosi: {rc2.calc_area()} cm2')

tp = Trapeze(7.5,5.2,4.4)
print(f'pole figury {tp.__class__.__name__} wynosi: {tp.calc_area()} cm2')

cr = Circle(5.5)
print(f'pole figury {cr.__class__.__name__} wynosi: {cr.calc_area():.2f} cm2')

