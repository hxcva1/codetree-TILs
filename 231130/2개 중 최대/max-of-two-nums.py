a = input().split()
a = list(map(int, a))

m = a[0] if a[0] > a[1] else a[1]
print(m)