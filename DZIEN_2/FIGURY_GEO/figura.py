from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self,a,b=None):
        self.a=a
        if b:
            self.b=b

    @abstractmethod
    def calc_area(self):
        pass
