import sys

INT_MAX = sys.maxsize

n = int(input())

arr = list(map(int,input().split()))

ret = INT_MAX
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += abs(i-j) * arr[j]
    ret = min(ret,cnt)
print(ret)