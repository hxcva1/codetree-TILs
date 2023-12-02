arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a <= b and a <= c:
    m = a
elif b <= c and b <= a:
    m = b
else:
    m = c
print(m)