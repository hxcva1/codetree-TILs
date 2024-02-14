n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

i = 1
x, y = 0, 0
c_dir = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m
while i <= n*m:
    arr[x][y] = i
    nx, ny = x + dxs[c_dir], y + dys[c_dir]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        c_dir = (c_dir + 1) % 4
    x, y = x + dxs[c_dir], y + dys[c_dir]
    i += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()