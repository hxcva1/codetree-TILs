n = int(input())

class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

students = []
for i in range(n):
    h, w = tuple(input().split())
    students.append(Student(int(h), int(w), i+1))

students.sort(key=lambda x : (-x.h, -x.w, x.num))

for student in students:
    print(student.h, student.w, student.num)