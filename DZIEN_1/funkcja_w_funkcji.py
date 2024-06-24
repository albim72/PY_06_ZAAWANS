print("programowanie funkcyjne")

#przykład1
def witaj(imie:str)->str:
    return f'Miło Cię widzieć {imie}!'


print(witaj("Konrad"))
print(witaj(12345))

def konkurs(imie,punkty,miejsce):
    return f'uczestnik konkursu {imie}, liczba punktów: {punkty}, miejsce: {miejsce}'

def bonus(punkty,bonus):
    if punkty > 60:
        return punkty + bonus
    else:
        return punkty

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Anna",67,12))
print(osoba(bonus,80,10))
print(osoba(bonus,34,10))
