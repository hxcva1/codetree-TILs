a = input().split()
a = list(map(int, a))

if a[0] > a[1] and a[0] < a[2] or a[0] > a[2] and a[0] < a[1]:
    print(a[0])
elif a[1] > a[0] and a[1] < a[2] or a[1] > a[2] and a[1] < a[0]:
    print(a[1])
else:
    print(a[2])