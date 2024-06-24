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

#przykład 2
def rejestracja(oplata):
    def lista(nr):
        return f'jesteś na startowej, zawodnik nr {nr}'
    def brak():
        return 'brak wplaty, uzupełnij w ciągu 3 dni'
    def error():
        return 'błąd w opłacie -> ponów'
    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(1)(456))
print(rejestracja(0)())
print(rejestracja(12)())

# przykład 3
print("Calculations")
def calculation(func, a, b):
    return func(a, b)

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

# Example calls
addition_result = calculation(addition, 5, 3)
subtraction_result = calculation(subtraction, 5, 3)
multiplication_result = calculation(multiplication, 5, 3)

print(f"Addition result: {addition_result}")
print(f"Subtraction result: {subtraction_result}")
print(f"Multiplication result: {multiplication_result}")

