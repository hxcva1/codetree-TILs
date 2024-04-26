import sys

n, h, t = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n-t+1):
    tmp = arr[i:i+t]
    cost = 0
    for elem in tmp:
        cost += abs(elem - h)
    ans = min(ans,cost)
print(ans)