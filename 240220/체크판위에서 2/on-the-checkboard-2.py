r, c = tuple(map(int, input().split()))

arr = [
    input().split()
    for _ in range(r)
]

def f(x, y, cnt, now):
    if x == r - 1 and y == c - 1 and cnt == 3:
        global ret
        ret += 1 
        return
    if cnt > 2:
        return
    for i in range(x + 1, r):
        for j in range(y + 1, c):
            if now == "W":
                if arr[i][j] == "B":
                    f(i,j,cnt+1,"B")
            else:
                if arr[i][j] == "W":
                    f(i,j,cnt+1,"W")

ret = 0
f(0,0,0,arr[0][0])
print(ret)