n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    for j in range(n-2):
        cnt = 0
        cnt += arr[i][j] + arr[i][j+1] + arr[i][j+2]
        nx, ny = i, j+3
        while nx < n:
            while ny < n-2:
                cnt2 = 0
                cnt2 += arr[nx][ny] + arr[nx][ny+1] + arr[nx][ny+2]
                ans = max(ans, cnt+cnt2)
                ny += 1
            nx += 1
            ny = 0
print(ans)