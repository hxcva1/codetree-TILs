import sys

ret = -sys.maxsize

n, k = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

for i in range(n - k + 1):
    sum_val = 0
    for j in range(i, i+k):
        sum_val += arr[j]
    ret = max(ret, sum_val)
print(ret)