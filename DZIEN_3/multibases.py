def logger(self,m,n):
    return f"{m}: {n}"

class MultiBases(type):
    def __new__(cls,classname,bases,attrs):
        if len(bases)>1:
            raise TypeError('wielodziedziczenie jest zabronione!')
        return super().__new__(cls,classname,bases,attrs)

    def __init__(self,classname,bases,attrs):
        self.logger = logger


class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(A):
    pass

class Ekstra:
    pass

b = B()
print(f'{b.logger(34,'info')}')

# e = Ekstra
# print(f'{e.logger(34,'info')}')

# class Test(Ekstra,B):
#     pass

def policz(self,x,y):
    return x*y-10

B.logger = policz
c = B()
print(c.logger(27,66))

a = A()
print(a.logger(56,7))
