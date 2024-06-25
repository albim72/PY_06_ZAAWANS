# import osoba as os
from osoba import Osoba

os1 = Osoba("Jan",46,102,173)
print(os1)
nlat = 8
print(f'wiek za {nlat} lat: {os1.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {os1.czypracownik()}')

print("_"*50)
os2 = Osoba("Anna",33,54,170)
os2.set_kolor_oczu("niebieskie")
print(os2)
print(f"zmieniony kolor oczu -> {os2.get_kolor_oczu()}")
nlat = 5
print(f'wiek za {nlat} lat: {os2.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {os2.czypracownik()}')
