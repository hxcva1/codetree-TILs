a = input().split()
a = list(map(int, a))

for _ in range(a[1]):
    print(a[0]+a[1])
    a[0] += a[1]