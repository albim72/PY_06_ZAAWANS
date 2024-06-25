from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    @abstractmethod
    def calc_area(self):
        pass
