n = input()

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

c_dir = 2

x, y = 0, 0
cnt = 0
flag = 0
for elem in n:
    cnt += 1
    if elem == "R":
        c_dir = (c_dir + 1) % 4
    elif elem == "L":
        c_dir = (c_dir -1 + 4) % 4
    else:
        x, y = x + dxs[c_dir], y + dys[c_dir]
    if x == 0 and y == 0:
        flag = 1
        break
if flag:
    print(cnt)
else:
    print(-1)