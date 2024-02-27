n, k = tuple(map(int, input().split()))

arr = [0] * (10002)
for _ in range(n):
    loc, a = input().split()
    if a == "G":
        arr[int(loc)] = 1
    else:
        arr[int(loc)] = 2

ret = 0

for i in range(1,10000 - k + 2):
    val = 0
    for j in range(i, i+k+1):
        val += arr[j]
    ret = max(ret, val)

print(ret)