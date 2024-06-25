from abc import ABC, abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,m):
        return f'metoda nieasbstrakcyjna: {m}'

    #klasyczna pusta metoda abstrakcyjna
    @abstractmethod
    def policz(self):
        pass

    #metoda abstrakcyjna z ciałem domyślnym
    @abstractmethod
    def policz_x(self):
        return self.x*7


class Regular(Prototyp):

    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 1005

    def policz_x(self):
        return super().policz_x() + self.y*5


reg = Regular(4,7)
print(f'metoda policz -> {reg.policz()}')
print(f'metoda policz_x -> {reg.policz_x()}')
print(reg.msg("abcdfg"))
