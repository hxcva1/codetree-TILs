n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

ret = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            x, y = i + dx, j + dy
            if in_range(x, y) and arr[x][y] == 1:
                cnt += 1
        if cnt >= 3:
            ret += 1
print(ret)