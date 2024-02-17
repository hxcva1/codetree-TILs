n = int(input())

arr = [
    [0] * n
    for _ in range(n)
]

for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == "/":
            arr[i][j] = 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def next_dir(now, mirror):
    if mirror == 0:
        if now == 0:
            return 1
        elif now == 1:
            return 2
        elif now == 2:
            return 3
        else:
            return 0
    else:
        if now == 0:
            return 3
        elif now == 1:
            return 2
        elif now == 2:
            return 1
        else:
            return 0
x, y = 0, 0
cnt = 0
c_dir = 0
k = int(input())
if k // 4 == 0:
    x = 0
    y = (k - 1) % n
    c_dir = 1
elif k // 4 == 1:
    y = n - 1
    x = y = (k - 1) % n
    c_dir = 2
elif k // 4 == 2:
    x = n - 1
    y = (n - k % n) % n
    c_dir = 3
else:
    y = 0
    x = (n - k % n) % n
    c_dir = 0

while in_range(x, y):
    cnt += 1
    c_dir = next_dir(c_dir, arr[x][y])
    x, y = x + dxs[c_dir], y + dys[c_dir]
print(cnt)