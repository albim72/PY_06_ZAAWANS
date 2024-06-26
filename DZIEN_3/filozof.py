odp = input("Czy Ziemia jest płaska? Czy chcesz znac odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def brak(self):
    return "brak odpowiedzi..."

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak


class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

fil1 = Arystoteles()
fil2 = Platon()
fil3 = SwTomasz()
print(f'filozof: {fil1.__class__.__name__} twierdzi: {fil1.odpowiedz()}')
print(f'filozof: {fil2.__class__.__name__} twierdzi: {fil2.odpowiedz()}')
print(f'filozof: {fil3.__class__.__name__} twierdzi: {fil3.odpowiedz()}')
