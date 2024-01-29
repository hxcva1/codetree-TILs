n = int(input())

students = []
for i in range(n):
    h, w = tuple(map(int, input().split()))
    students.append((h,w,i+1))

students.sort(key=lambda x : (x[0], -x[1]))
for s in students:
    print(s[0], s[1], s[2])