n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

ret = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            for k in range(i,i+3):
                for l in range(j, j+3):
                    if k >= n or l >= n:
                        cnt = 0
                        break
                    if arr[k][l] == 1:
                        cnt += 1
            ret = max(ret, cnt)
print(ret)