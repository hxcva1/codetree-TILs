n, t = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

cnt, ret = 0, 0

for i in range(n):
    if arr[i] <= t:
        cnt = 0
    else:
        cnt += 1
    ret = max(cnt, ret)
print(ret)