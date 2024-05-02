n, r, c = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visit = [
    [0] * n
    for _ in range(n)
]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]
max_pos = (-1, -1)
max_num = arr[r-1][c-1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
cur_pos = (r-1, c-1)
print(max_num, end=' ')
while 1:
    tmp = cur_pos
    for dx, dy in zip(dxs, dys):
        nx = cur_pos[0] + dx
        ny = cur_pos[1] + dy
        if in_range(nx, ny) and visit[nx][ny] == 0 and arr[nx][ny] > max_num:
            max_num = arr[nx][ny]
            print(max_num, end=' ')
            visit[nx][ny] = 1
            cur_pos = (nx, ny)
    if cur_pos == tmp:
        break