class InFloatValueError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f'wartośc {self.value} jest niewłaściwa! Akceptowalne są tylko wartości w typie: int i float'


class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return (f"klucze i wartości winy byc przekazane w listach lub krotkach..."
                f"klucz: {self.key} jest w typie {type(self.key)},"
                f"wartośc: {self.value} jest w typie {type(self.value)}")
