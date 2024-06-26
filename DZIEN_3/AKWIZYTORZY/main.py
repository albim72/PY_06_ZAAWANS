from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class DuzaFirma:
    def __repr__(self):
        return "wlaściciel firmy otrzymuje wypłatę dywidendy na podstawie zysków firmy za ubiegły okres..."

    def zarobek(self):
        return Decimal('10_000_000')

df = DuzaFirma()
ak = Akwizytor('Jan','Kot',754345456,Decimal('516_758'),Decimal('9.2'))
aet = AkwizytorNaEtacie('Anna','Nowak',8574645,Decimal('499_800'),
                        Decimal('7.6'),Decimal('5_200'))

pracownicy = [ak,aet,df]
for pr in pracownicy:
    print(pr)
    print(f'{pr.zarobek():,.2f} zł\n')
