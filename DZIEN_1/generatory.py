#przykład 1

def liczby():
    for i in range(17):
        yield i*3

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)
