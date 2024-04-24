import sys
n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
sum_all = sum(arr)
ans = sys.maxsize

for i in range(n-1):
    for j in range(i+1,n):
        ans = min(ans, abs(s-(sum_all-arr[i]-arr[j])))
print(ans)