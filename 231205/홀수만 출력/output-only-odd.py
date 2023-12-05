a = input().split()
a = list(map(int, a))

for i in range(a[0], a[1] + 1, 2):
    print(i, end=' ')