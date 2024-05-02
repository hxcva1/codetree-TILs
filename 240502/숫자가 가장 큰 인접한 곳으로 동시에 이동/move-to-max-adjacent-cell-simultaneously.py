n, m, t = tuple(map(int , input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def simulation(x, y, count, max_locs):
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    max_num = arr[x][y]
    max_loc = (x,y)
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx,ny) and arr[nx][ny] > max_num:
            max_num = arr[nx][ny]
            max_loc = (nx, ny)

    max_locs.append(max_loc)
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
    max_locs = []
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                simulation(i,j, count, max_locs)
                
    for i in range(n):
        for j in range(n):
            count[i][j] = 0
    for x, y in max_locs:
        count[x][y] += 1

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