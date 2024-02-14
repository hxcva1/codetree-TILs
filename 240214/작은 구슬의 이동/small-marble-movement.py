n, t = tuple(map(int, input().split()))

r, c, d = input().split()

dxs, dys = [1, 0, -1, 0,], [0, 1, 0, -1]
mapper = {
    'U' : 2,
    'D' : 0,
    'R' : 1,
    'L' : 3,
}

c_dir = mapper[d]
def in_range(x, y):
    return 0 < x and x <= n and 0 < y and y <= n

x, y = int(r), int(c)
for _ in range(t):
    nx, ny = x + dxs[c_dir], y + dys[c_dir]
    if not in_range(nx, ny):
        c_dir = (c_dir + 2) % 4
        continue
    x, y = nx, ny
print(x,y)