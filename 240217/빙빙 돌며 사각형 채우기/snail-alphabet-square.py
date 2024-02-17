c = chr(ord("A"))

n, m = map(int, input().split())

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

c_dir = 3

arr = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

now = ord("A")
x, y = 0, 0
for _ in range(n*m):
    if now > ord("Z"):
        now = ord("A")
    arr[x][y] = chr(now)
    nx, ny = x + dxs[c_dir], y + dys[c_dir]
    if (not in_range(nx, ny)) or arr[nx][ny] != 0:
        c_dir = (c_dir + 1) % 4
    x, y = x + dxs[c_dir], y + dys[c_dir]
    now += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()