n, m, t = tuple(map(int , input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def simulation(x, y, count):
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx,ny) and arr[nx][ny] > arr[x][y]:
            count[x][y] -= 1 
            count[nx][ny] += 1
            return


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
    
count = [
    [0] * n
    for _ in range(n)
]
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    count[r-1][c-1] = 1

for _ in range(t):
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                simulation(i,j, count)
    for i in range(n):
        for j in range(n):
            if count[i][j] > 1:
                count[i][j] = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            cnt += 1
print(cnt)