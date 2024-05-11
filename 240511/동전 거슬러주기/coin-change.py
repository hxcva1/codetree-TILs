N, M = map(int, input().split())

coins = list(map(int, input().split()))

dp = [2147483647] * (M+1)
dp[0] = 0
for i in range(M+1):
    for j in range(N):
        if i >= coins[j] and dp[i-coins[j]] != 2147483647:
            dp[i] = min(dp[i], dp[i-coins[j]] + 1)
if dp[M] == 2147483647:
    print(-1)
else:
    print(dp[M])