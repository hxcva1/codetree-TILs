n = int(input())

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

c_dir = 1

arr = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

x, y = n-1, n-1
now = n * n
for _ in range(n*n):
    arr[x][y] = now
    nx, ny = x + dxs[c_dir], y + dys[c_dir]
    if (not in_range(nx, ny)) or arr[nx][ny] != 0:
        c_dir = (c_dir +1) % 4
    x, y = x + dxs[c_dir], y + dys[c_dir]
    now -= 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()