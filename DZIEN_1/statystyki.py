liczby = [877,34,56,-122,4,1,66,-234,135,689,1111,0,-988,1.22,89,13,56,1356,-345,-1000,16,19]

def pokaz_statystyki(dane:list)->tuple:
    minimum:float = min(dane)
    maksimum:float = max(dane)
    roztep:float = maksimum - minimum
    sr_arytm:float = sum(dane)/len(dane)
    return minimum,maksimum,roztep,sr_arytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,srednia = pokaz_statystyki(liczby)
print(f'wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, średnia: {srednia}')
