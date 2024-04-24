n, m = tuple(map(int, input().split()))

dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

arr = [
    list(input())
    for _ in range(n)
]
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m
ans = 0
for i in range(n):
    for j in range(m):
        if (arr[i][j] == "L"):
            for dx, dy in zip(dxs, dys):
                if in_range(i+dx, j+dy) and arr[i+dx][j+dy] == "E" and in_range(i+2*dx, j+2*dy) and arr[i+2*dx][j+2*dy] == "E":
                    ans += 1
print(ans)