class Kolor:
    def __call__(self,k,b):
        return 200*k-b

k = Kolor()
print(k)

print(k(4,6))
