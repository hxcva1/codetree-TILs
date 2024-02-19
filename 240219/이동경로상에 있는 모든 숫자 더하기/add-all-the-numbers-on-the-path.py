n, t = map(int, input().split())

s = input()
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

c_dir = 2

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

x, y = n // 2, n // 2
cnt = 0
cnt += arr[x][y]
for elem in s:
    if elem == "R":
        c_dir = (c_dir + 1) % 4
    elif elem == "L":
        c_dir = (c_dir -1 + 4) % 4
    else:
        nx, ny = x + dxs[c_dir], y + dys[c_dir]
        if not in_range(nx, ny):
            continue
        x, y = x + dxs[c_dir], y + dys[c_dir]
        cnt += arr[x][y]
print(cnt)