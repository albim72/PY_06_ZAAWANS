from homework import Homework
from exam import Exam
from grade import ExamD

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

print("_________ EXAM D_________")
first = ExamD()
first.math_grade = 34
first.alg_grade = 45
first.prog_grade = 55

print(f'pierwsze podejście -> \nmatematyka -> {first.math_grade}\nalgorytmika -> {first.alg_grade}\n'
      f'programowanie {first.prog_grade}')

second = ExamD()
second.math_grade = 64
second.alg_grade = 73
second.prog_grade = 88

print("_" * 50)
print(f'drugie podejście -> \nmatematyka -> {second.math_grade}\nalgorytmika -> {second.alg_grade}\n'
      f'programowanie {second.prog_grade}')

print("_" * 50)
print(f'Archiwum --> pierwsze podejście -> \nmatematyka -> {first.math_grade}\nalgorytmika -> {first.alg_grade}\n'
      f'programowanie {first.prog_grade}')
