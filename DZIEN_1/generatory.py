#przykład 1

def liczby():
    for i in range(17):
        yield i*3

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)


#przyklad 2

def resumption(n,k):
    print("wstrzymanie działania 0")
    yield 1003
    print("wznowienie działania 1")
    yield n+k
    print("wstrzymanie działania 1")
    yield n-k
    print("wznowienie działania 2")
    print("wstrzymanie działania 2")
    n = 8*k-2
    k=3*k
    yield n*k
    print("wznowienie działania 3")
    print("wstrzymanie działania 3")
    yield n/k
    print("wznowienie działania 4")
    yield "to jest ostatni element generatora"

print(resumption(7,8))
print(tuple(resumption(7,8)))
print("_"*50)
for i in resumption(7,8):
    print("*"*35)
    print(type(i))
    print(f'zwrócono wartośćL {i}')
print("_"*50)
