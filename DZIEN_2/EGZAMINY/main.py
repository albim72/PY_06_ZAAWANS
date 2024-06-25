from homework import Homework
from exam import Exam

print("_________ HOMEWORK _________")
g = Homework()
g.grade = 95
assert not(g.grade >= 5 and g.grade <=15)
print(f'ocena za projekt: {g.grade}')

print("_________ EXAM _________")
ex = Exam()
ex.part_a_grade = 72
ex.part_b_grade = 79

assert ex.part_a_grade >= 70
assert ex.part_b_grade >= 50

print(f'egzamin -> a -> {ex.part_a_grade}, b -> {ex.part_b_grade}')
