from homework import Homework

print("_________ HOMEWORK _________")
g = Homework()
g.grade = 95
assert not(g.grade >= 5 and g.grade <=15)
print(f'ocena za projekt: {g.grade}')
