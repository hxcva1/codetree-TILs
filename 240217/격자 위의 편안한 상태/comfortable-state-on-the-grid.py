n, m = map(int, input().split())

arr = [
    [0] * n
    for _ in range(n)
]
dxs, dys = [1, 0, -1, 0], [0, 1, -0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    cnt = 0
    arr[x-1][y-1] = 1
    for dx, dy in zip(dxs, dys):
        if in_range(x+dx-1,y+dy-1) and arr[x+dx-1][y+dy-1] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)