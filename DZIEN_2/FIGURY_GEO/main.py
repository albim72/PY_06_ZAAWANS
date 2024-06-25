from triangle import Triangle
from rectangle import Rectangle

tr = Triangle(5.6,7.2)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.calc_area()} cm2')

rc1 = Rectangle(4,5.8)
print(f'pole figury {rc1.__class__.__name__} wynosi: {rc1.calc_area()} cm2')

rc2 = Rectangle(5.5,5.5)
print(f'pole figury {rc2.__class__.__name__} wynosi: {rc2.calc_area()} cm2')
