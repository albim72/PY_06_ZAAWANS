from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"pełna nazwa matody: {func.__qualname__}")
        return func(*args,**kwargs)

    return wrapper


def debugmethods(cls):

    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

class DebugMeta(type):

    def __new__(cls, clsname,bases,attrs):
        obj = super().__new__(cls, clsname,bases,attrs)
        obj = debugmethods(obj)
        return obj

class Base(metaclass=DebugMeta):pass

class CalcAdd(Base):
    def add(self,x,y):
        return x+y

class CalcMul(Base):
    def mul(self,x,y):
        return x*y

mc = CalcAdd()
print(mc.add(3,7))

ml = CalcMul()
print(ml.mul(3,7))
