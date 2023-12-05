a = input().split()
b = input().split()
c = input().split()
a[1] = int(a[1])
b[1] = int(b[1])
c[1] = int(c[1])

n = 0

if a[0] == "Y" and a[1] >= 37:
    n += 1
if b[0] == "Y" and b[1] >= 37:
    n += 1
if c[0] == "Y" and c[1] >= 37:
    n += 1
if n >= 2:
    print("E")
else:
    print("N")