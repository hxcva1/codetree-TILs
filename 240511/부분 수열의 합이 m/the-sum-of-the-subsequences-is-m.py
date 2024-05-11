N, M = map(int, input().split())

arr = list(map(int, input().split()))

# dp[i] 합이 i 가 되는 경우 최소 부분 수열의 길이
dp = [2147483647] * (M+1)

dp[0] = 0

for i in range(N):
    for j in range(M, -1, -1):
        if j >= arr[i] and dp[j-arr[i]] != 2147483647:
            dp[j] = min(dp[j], dp[j-arr[i]] + 1)
if dp[M] == 2147483647:
    print(-1)
else:
    print(dp[M])