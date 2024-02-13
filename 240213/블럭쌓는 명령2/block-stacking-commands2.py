n, k = map(int, input().split())
arr = [0 for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a-1,b):
        arr[i] += 1
ret = -1
for i in range(n):
    ret = max(ret, arr[i])
print(ret)