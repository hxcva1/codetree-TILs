dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())

cx, cy = 0, 0
for _ in range(n):
    d, t = tuple(input().split())
    if d == "N":
        cx = cx + dx[1]*int(t)
        cy = cy + dy[1]*int(t)
    elif d == "S":
        cx = cx + dx[3]*int(t)
        cy = cy + dy[3]*int(t)
    elif d == "W":
        cx = cx + dx[2]*int(t)
        cy = cy + dy[2]*int(t)
    else:
        cx = cx + dx[0]*int(t)
        cy = cy + dy[0]*int(t)
print(cx, cy)