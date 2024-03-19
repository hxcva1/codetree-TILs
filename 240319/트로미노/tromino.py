block = [[(0,0), (1,0), (1,-1)], [(0,0), (1,0), (1,1)], [(0,0), (0,-1), (1,-1)], [(0,0), (0,1), (1,1)], [(0,0), (0,1), (0,2)], [(0,0), (1,0), (2,0)]]

n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

ret = 0
for i in range(n):
    for j in range(m):
        for k in range(6):
            cnt = 0
            for nx, ny in block[k]:
                if i+nx >= n or j+ny >= m:
                    cnt = 0
                    break
                cnt += arr[i+nx][j+ny]
            ret = max(ret, cnt)

print(ret)