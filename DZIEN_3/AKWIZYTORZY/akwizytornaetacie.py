from akwizytor import Akwizytor
from decimal import Decimal

class AkwizytorNaEtacie(Akwizytor):
    """
        akwizytor na etacie - pracownik, którego wynagrodzenie
        jest prowizją od sprzedaży oraz stałej pensji
        """

    def __init__(self, imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja,pensja):
        super().__init__(imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja)
        self.pensja = pensja
        
    def __repr__(self):
        return f'etatowy:\n{super().__repr__()}\nryczałt(pensja): {self.pensja:.2f} zł\n'

    @property
    def pensja(self):
        return self._pensja

    @pensja.setter
    def pensja(self,kwota):
        if kwota <= Decimal('0.00'):
            raise ValueError('wynagrodzenie musi byc dodatnie!')
        self._pensja = kwota
