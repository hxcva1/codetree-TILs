class Student:
    def __init__(self, name, k, y, s):
        self.name = name
        self.k = k
        self.y = y
        self.s = s

n = int(input())

students = []
for _ in range(n):
    name, k, y, s = tuple(input().split())
    students.append(Student(name, int(k), int(y), int(s)))


students.sort(key=lambda x: (-x.k, -x.y, -x.s))

for student in students:
    print(student.name, student.k, student.y, student.s)