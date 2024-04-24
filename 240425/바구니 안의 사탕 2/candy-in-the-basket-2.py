n, k = tuple(map(int, input().split()))

arr = [0] * 101

for _ in range(n):
    candy, bucket = tuple(map(int, input().split()))
    arr[bucket] += candy

ans = 0
for i in range(101):
    if i - k < 0:
        l = 0
    else:
        l = i - k
    if i + k >= 101:
        r = 100
    else:
        r = i + k
    tmp = arr[l:r+1]
    ans = max(ans, sum(tmp))
print(ans)