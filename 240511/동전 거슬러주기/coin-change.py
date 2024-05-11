N, M = map(int, input().split())

coins = list(map(int, input().split()))

dp = [2147483647] * (M+1)
dp[0] = 0
for i in range(M+1):
    for j in range(N):
        # 갱신하려는 값이 갱신되지 않은 값을 사용하면 안된다
        if i >= coins[j] and dp[i-coins[j]] != 2147483647:
            dp[i] = min(dp[i], dp[i-coins[j]] + 1)
if dp[M] == 2147483647:
    print(-1)
else:
    print(dp[M])