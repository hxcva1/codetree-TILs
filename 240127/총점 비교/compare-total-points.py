n = int(input())

students = []

for _ in range(n):
    name, p1, p2, p3 = tuple(input().split())
    students.append((name, int(p1), int(p2), int(p3)))

students.sort(key=lambda x : x[1]+x[2]+x[3])

for elem in students:
    print(elem[0], elem[1], elem[2], elem[3])