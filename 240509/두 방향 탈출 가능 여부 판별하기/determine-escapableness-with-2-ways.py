N, M = map(int, input().split())

dx, dy = [1, 0], [0, 1]
board = [
    list(map(int, input().split()))
    for _ in range(N)
]

visit = [
    [0] * (M)
    for _ in range(N)
]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M 

ans = 0
def dfs(x, y):
    global ans
    if x == N-1 and y == M-1:
        ans = 1
        return
    for nx, ny in zip(dx, dy):
        nxt_x, nxt_y = x + nx, y + ny
        if in_range(nxt_x, nxt_y) and board[nxt_x][nxt_y] == 1 and visit[nxt_x][nxt_y] == 0:
            visit[nxt_x][nxt_y] = 1
            dfs(nxt_x, nxt_y)

dfs(0, 0)
visit[0][0] = 1
print(ans)