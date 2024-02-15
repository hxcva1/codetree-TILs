n = int(input())

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
mapper = {
    'N' : 2,
    'S' : 0,
    'E' : 1,
    'W' : 3
}

x, y = 0, 0
cnt = 0
flag = 0
for _ in range(n):
    d, t = input().split()
    for _ in range(int(t)):
        x = x + dxs[mapper[d]]
        y = y + dys[mapper[d]]
        cnt += 1
        if x == 0 and y == 0:
            flag = 1
            break
    if flag:
        break
if flag:
    print(cnt)
else:
    print(-1)