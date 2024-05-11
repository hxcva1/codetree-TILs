n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0] * (n+1)
    for _ in range(n+1)
]
dp[0][0] = arr[0][0]

for i in range(n):
    for j in range(n):
        if i != n-1:
            dp[i+1][j] = max(dp[i+1][j], arr[i+1][j] + dp[i][j])
        if j != n-1:
            dp[i][j+1] = max(dp[i][j+1], arr[i][j+1] + dp[i][j])

print(dp[n-1][n-1])