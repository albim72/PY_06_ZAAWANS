import random
import types

def notify(fn,*args,**kwargs):
    def fncomposite(*args,**kwargs):
        print(f'{fn.__name__} została uruchomiona...')
        rt = fn(*args,**kwargs)
        return rt
    return fncomposite

#fncomposite -> wrapper

class Notifies(type):
    def __new__(cls,clsnames,bases,attrs):
        for name,value in attrs.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attrs[name] = notify(value)
        return super(Notifies,cls).__new__(cls,clsnames,bases,attrs)

class MyMath(metaclass=Notifies):
    def multi(a,b,c):
        p=a*b*c
        print(p)
        return p

    def policz(self,x,y):
        w = x/y*100
        print(w)
        return w

    @property
    def differ(self):
        return 3344



MyMath.multi(5,36,7)
mm = MyMath()
mm.policz(8.8,4)

print(MyMath.differ)

print(mm.differ)

class Info(metaclass=Notifies):
    def intro(self):
        print("nowe kody: 48573856735476483")

im = Info()
im.intro()

class NewCl(Info):
    def random_nb(self):
        return random.random()

nc = NewCl()
print(nc.random_nb())
