from xyz.kolory import Colors
class MyMeta(type):
    def __new__(cls,clsname,superclasses,attrs):
        #clsname - nazwa klasy
        #superclasses - wszystkie klasy dziedziczone w pierwszym rzędzie
        #attrs - wszystkie atrybuty klasy: zmienne, stałe, metody, właściwości... etc.
        print(f'nazwa klasy: {clsname}')
        print(f'klasy dziedziczone: {superclasses}')
        print(f'atrybuty klasy: {attrs}')
        return type.__new__(cls,clsname,superclasses,attrs)

    def one(cls):
        return 1

class S:
    pass

class F:
    pass

class Special(S,Colors,metaclass=MyMeta):
    pass

class B(F,Special):
    def __new__(cls, *args, **kwargs):
        print("inna opcja...")
        return object.__new__(B)
    def __repr__(self):
        return "nowa reprez..."
class Normal():
    def msg(self,m):
        return "abc@qq.pl"

class NextC(B,Normal):
    def msg(self, m):
        return super().msg(m)


cf = NextC
print(cf.one())

# ob = NextC()
# print(ob.one())
