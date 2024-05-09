from collections import deque

N, M = map(int, input().split())

board = [
    list(map(int, input().split()))
    for _ in range(N)
]

visit = [
    [0] * M
    for _ in range(N)
]

q = deque()

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x,y):
    return 0 <= x and x < N and 0 <= y and y < M

def push(x, y, q, num):
    visit[x][y] = num + 1
    q.append((x,y))

push(0,0, q, 0)

def bfs(q):
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and visit[nx][ny] == 0 and board[nx][ny]:
                push(nx,ny,q, visit[x][y])
    
bfs(q)

print(visit[N-1][M-1] -1)