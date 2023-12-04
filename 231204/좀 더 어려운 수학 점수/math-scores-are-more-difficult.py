a = input().split()
a = list(map(int,a))
b = input().split()
b = list(map(int,b))

if a[0] > b[0]:
    print("A")
elif a[0] < b[0]:
    print("B")
elif a[1] > b[1]:
    print("A")
else:
    print("B")