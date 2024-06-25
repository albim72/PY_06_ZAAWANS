class PositiveTuple(tuple):
    def __new__(cls,*numbers):
        skipped = 0
        pos_numbers = []
        for x in numbers:
            if x >= 0:
                pos_numbers.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls,pos_numbers)
        instance._skipped = skipped
        return instance

pos = PositiveTuple(9,25,5,-5,0,22,-45,2,5,-6,3,-77,-4,-2,6,8)
print(type(pos))
print(pos)
print(pos._skipped)
