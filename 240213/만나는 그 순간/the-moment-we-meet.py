n, m = tuple(map(int, input().split()))

a = [0] * (1000000)
b = [0] * (1000000)

pos = 0
i = 0
for _ in range(n):
    d, t = input().split()
    if d == "R":
        for j in range(int(t)):
            a[i] = pos
            pos += 1
            i += 1
    else:
        for j in range(int(t)):
            a[i] = pos
            pos -= 1
            i += 1
movea = i
pos = 0
i = 0
for _ in range(m):
    d, t = input().split()
    if d == "R":
        for j in range(int(t)):
            b[i] = pos
            pos += 1
            i += 1
    else:
        for j in range(int(t)):
            b[i] = pos
            pos -= 1
            i += 1
moveb = i
flag = 1
for j in range(1,min(movea, moveb)):
    if a[j] == b[j]:
        print(j)
        flag = 0
        break
if flag:
    print(-1)