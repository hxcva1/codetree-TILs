import sys

n, h, t = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n-t+1):
    tmp = arr[i:i+t]
    mx = max(tmp)
    mn = min(tmp)
    for heights in range(mn, mx+1):
        cost = 0
        for elem in tmp:
            cost += abs(elem - heights)
        ans = min(ans,cost)
print(ans)