n = int(input())

arr = list(map(int, input().split()))
ret = 0
for i in range(n-2):
    for j in range(i+2, n):
        ret = max(ret, arr[i] + arr[j])
print(ret)