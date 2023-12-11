a = input().split()
a = list(map(int , a))

for i in range(a[1], a[0]-1, -1):
    print(i, end=' ')